import os
import chainlit as cl
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes import SearchIndexClient
from llama_index.core import StorageContext, VectorStoreIndex
from llama_index.core.settings import Settings, CallbackManager
from llama_index.embeddings.azure_openai import AzureOpenAIEmbedding
from llama_index.llms.azure_openai import AzureOpenAI
from llama_index.vector_stores.azureaisearch import AzureAISearchVectorStore, IndexManagement
from llama_index.core.query_engine import CustomQueryEngine
from llama_index.multi_modal_llms.azure_openai import AzureOpenAIMultiModal
from llama_index.core.schema import ImageNode, NodeWithScore, MetadataMode
from llama_index.core.prompts import PromptTemplate
from llama_index.core.base.response.schema import Response
from llama_index.core.retrievers import BaseRetriever
from typing import Optional

# Load environment variables
load_dotenv()

# Environment Variables
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_CHAT_COMPLETION_DEPLOYED_MODEL_NAME = os.getenv("AZURE_OPENAI_CHAT_COMPLETION_DEPLOYED_MODEL_NAME")
AZURE_OPENAI_EMBEDDING_DEPLOYED_MODEL_NAME = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYED_MODEL_NAME")
SEARCH_SERVICE_ENDPOINT = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
SEARCH_SERVICE_API_KEY = os.getenv("AZURE_SEARCH_ADMIN_KEY")
INDEX_NAME = "llamaindex-azure-aisearch-rag"

# Initialize AzureOpenAIMultiModal for GPT-4o-mini
azure_openai_mm_llm = AzureOpenAIMultiModal(
    engine="gpt-4o-mini",
    api_version="2024-06-01",
    model="gpt-4o-mini",
    max_new_tokens=4096,
    api_key=AZURE_OPENAI_API_KEY,
    api_base=AZURE_OPENAI_ENDPOINT,
)

QA_PROMPT_TMPL = """\
Below we give parsed text from slides in parsed markdown format, as well as the image.

---------------------
{context_str}
---------------------
Given the context information and not prior knowledge, answer the query. Explain whether you got the answer
from the parsed markdown or raw text or image, and if there's discrepancies, and your reasoning for the final answer.

Query: {query_str}
Answer: """

QA_PROMPT = PromptTemplate(QA_PROMPT_TMPL)

class MultimodalQueryEngine(CustomQueryEngine):
    """Custom multimodal Query Engine for public blob storage."""

    qa_prompt: PromptTemplate
    retriever: BaseRetriever
    multi_modal_llm: AzureOpenAIMultiModal

    def __init__(self, qa_prompt: Optional[PromptTemplate] = None, **kwargs) -> None:
        """Initialize."""
        super().__init__(qa_prompt=qa_prompt or QA_PROMPT, **kwargs)

    def custom_query(self, query_str: str) -> Response:
        # Retrieve relevant nodes
        nodes = self.retriever.retrieve(query_str)

        # Log retrieval information for debugging purposes
        print(f"[DEBUG] Retrieved {len(nodes)} nodes.")

        # Create ImageNode items directly using the blob URLs
        image_nodes = []
        for n in nodes:
            if "image_path" in n.metadata:
                try:
                    image_nodes.append(
                        NodeWithScore(node=ImageNode(image_url=n.metadata["image_path"]))
                    )
                except Exception as e:
                    print(f"Warning: Failed to create ImageNode for {n.metadata['image_path']}: {str(e)}")
                    continue

        # Create context string from text nodes
        context_str = "\n\n".join(
            [node.get_content(metadata_mode=MetadataMode.LLM) for node in nodes]
        )
        
        # Format the prompt
        fmt_prompt = self.qa_prompt.format(context_str=context_str, query_str=query_str)

        # Log formatted prompt for debugging purposes
        print(f"[DEBUG] Formatted Prompt: {fmt_prompt}")

        # Get response from multimodal LLM
        llm_response = self.multi_modal_llm.complete(
            prompt=fmt_prompt,
            image_documents=[image_node.node for image_node in image_nodes],
        )

        return Response(
            response=str(llm_response),
            source_nodes=nodes,
            metadata={"text_nodes": nodes, "image_nodes": image_nodes},
        )

@cl.on_chat_start
async def setup():
    # Initialize Azure OpenAI models
    llm = AzureOpenAI(
        model=AZURE_OPENAI_CHAT_COMPLETION_DEPLOYED_MODEL_NAME,
        deployment_name=AZURE_OPENAI_CHAT_COMPLETION_DEPLOYED_MODEL_NAME,
        api_key=AZURE_OPENAI_API_KEY,
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        api_version="2024-08-01-preview",
        streaming=True
    )

    embed_model = AzureOpenAIEmbedding(
        model=AZURE_OPENAI_EMBEDDING_DEPLOYED_MODEL_NAME,
        deployment_name=AZURE_OPENAI_EMBEDDING_DEPLOYED_MODEL_NAME,
        api_key=AZURE_OPENAI_API_KEY,
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        api_version="2024-08-01-preview"
    )

    # Set up callback manager
    callback_manager = CallbackManager([cl.LlamaIndexCallbackHandler()])

    # Configure global settings
    Settings.llm = llm
    Settings.embed_model = embed_model
    Settings.callback_manager = callback_manager

    # Initialize search clients
    credential = AzureKeyCredential(SEARCH_SERVICE_API_KEY)
    index_client = SearchIndexClient(endpoint=SEARCH_SERVICE_ENDPOINT, credential=credential)

    # Initialize vector store
    vector_store = AzureAISearchVectorStore(
        search_or_index_client=index_client,
        index_name=INDEX_NAME,
        index_management=IndexManagement.VALIDATE_INDEX,
        id_field_key="id",
        chunk_field_key="parsed_text_markdown",
        embedding_field_key="embedding",
        embedding_dimensionality=1536,
        metadata_string_field_key="metadata",
        doc_id_field_key="doc_id",
        language_analyzer="en.lucene",
        vector_algorithm_type="exhaustiveKnn",
    )

    # Create storage context
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    # Create index
    index = VectorStoreIndex.from_documents([], storage_context=storage_context)

    # Set up custom multimodal query engine
    query_engine = MultimodalQueryEngine(
        retriever=index.as_retriever(
            similarity_top_k=3
        ),
        multi_modal_llm=azure_openai_mm_llm,
    )

    # Store query engine in user session
    cl.user_session.set("query_engine", query_engine)

    await cl.Message(
        content="Hello! I'm ready to help you perform Multimodal RAG using LlamaIndex, Azure AI Search, and Azure OpenAI over the State of AI 2024 Report. What would you like to know?",
        author="Assistant"
    ).send()

@cl.on_message
async def main(message: cl.Message):
    # Retrieve query engine from user session
    query_engine = cl.user_session.get("query_engine")

    # Perform the query using the custom multimodal query engine
    response = await cl.make_async(query_engine.custom_query)(message.content)

    # Log for debugging
    print(f"[DEBUG] Response received: {response.response}")

    # Send the response content
    await cl.Message(content=response.response, author="Assistant").send()

    # Send source references and images if available
    if hasattr(response, 'source_nodes') and response.source_nodes:
        source_text = "\n\nSources:\n"
        for idx, source in enumerate(response.source_nodes, 1):
            source_text += f"{idx}. {source.get_content(metadata_mode=MetadataMode.LLM)}...\n\n"
        
        if source_text.strip():
            await cl.Message(content=source_text, author="Assistant").send()

        # Send images separately if any
        for source in response.source_nodes:
            if 'image_path' in source.metadata:
                image_path = source.metadata['image_path']
                image = cl.Image(
                    url=image_path,
                    name=f"Image from page {source.metadata.get('page_num', 'unknown')}",
                    display="inline"
                )
                await cl.Message(content=f"Image from the source:", elements=[image], author="Assistant").send()

if __name__ == "__main__":
    cl.run()
