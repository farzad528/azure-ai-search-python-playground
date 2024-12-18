# Azure AI Search Python Playground 🌐

Welcome to the **Azure AI Search Python Playground**! This repository contains a collection of Jupyter notebooks designed to explore the various capabilities of Azure AI Search. You'll find experiments focused on vector search, retrieval-augmented generation (RAG), and other retrieval system tasks using OpenAI's embedding models. Each notebook is a standalone experiment with detailed explanations to help you understand the concepts and apply them in your own projects.

## 📓 Notebooks

This repository includes a diverse range of Jupyter notebooks demonstrating integrations and functionalities with Azure AI Search:

### Foundational Techniques and Embeddings
1. **[OpenAI Text-Embedding-3-Large Model Exploration](azure-ai-search-text-embedding-3-large.ipynb)**  
   Enhance search relevance using the OpenAI text-embedding-3-large model.

2. **[Cohere Embed-v3 Exploration](azure-ai-search-cohere-embed-v3.ipynb)**  
   Improve embeddings and retrieval quality with the Cohere Embed-v3 model.

3. **[Indexing and Querying CSV Data](azure-ai-search-csv.ipynb)**  
   Learn how to index and query CSV datasets in Azure AI Search.

4. **[Document Boosting Techniques](azure-ai-search-document-boosting.ipynb)**  
   Influence relevance scoring with document boosting strategies.

5. **[Quantization Techniques](azure-ai-search-scalar-quantization.ipynb)**  
   Optimize efficiency and performance through advanced quantization.
   
5. **[Maximum Marginal Relevance](azure-ai-search-maximum-marignal-relevance.ipynb)**  
   Post-Process Vector Search Results using MMR (Maximum Marginal Relevance)

### RAG Evaluations and Quality Measurement
6. **[RAG Evaluation with Tonic AI](azure-ai-search-rag-eval-tonic-ai.ipynb)**  
   Assess Retrieval Augmented Generation (RAG) performance with Tonic AI Validate.

7. **[RAG Evaluation with TruLens](azure-ai-search-rag-eval-trulens.ipynb)**  
   Gain insights into RAG solutions using TruLens.

8. **[RAG Evaluation with Arize Phoenix](azure-ai-search-rag-eval-arize-ai.ipynb)**  
   Monitor and improve RAG quality with Arize Phoenix analytics.

9. **[Measuring Search Relevance with Ranx](azure-ai-search-eval-ranx.ipynb)**  
   Benchmark and quantify search relevance using Ranx.

10. **[RAG Evaluation with LlamaIndex, Literal AI, and RAGAS](azure-ai-search-literal-ai-ragas.ipynb)**  
    Refine and validate RAG pipelines using LlamaIndex, Literal AI logs, and RAGAS metrics.

### Advanced Workflows, Agents, and Multimodal Scenarios
11. **[LlamaIndex Workflows](azure-ai-search-llamaindex-workflows.ipynb)**  
    Orchestrate asynchronous search workflows with LlamaIndex and Azure AI Search.

12. **[NVIDIA RAG with LlamaIndex](azure-ai-search-nvidia-rag.ipynb)**  
    Build advanced RAG pipelines leveraging NVIDIA NIM embeddings and LlamaIndex.

13. **[Multimodal RAG using Contextual Retrieval](azure-ai-search-contextual-retreival.ipynb)**  
    Integrate LlamaParse Premium, Azure OpenAI, and Arize Phoenix for multimodal retrieval.

14. **[OpenAI Swarm Multi-Agent](azure-ai-search-openai-swarm.ipynb)**  
    Experiment with multi-agent capabilities using the OpenAI Swarm framework.

15. **[Getting Started with Voyage Multimodal Embeddings](azure-ai-search-voyage-multimodal)**  
    Explore voyage-multimodal-3 embeddings for combined text-image retrieval.

### Domain-Specific Agents and Applications
17. **[Legal AI Agent with CrewAI](azure-ai-search-legal-ai-agent.ipynb)**  
    Build a CrewAI Agent for complex legal queries, integrating Azure AI Search and Azure OpenAI.

18. **[Medical AI Agent with CrewAI](azure-ai-search-medical-ai-agent.ipynb)**  
    Develop a multi-agent medical assistant for cardiology scenarios.

18. **[Insurance Claims Agent with Semantic Kernel](azure-ai-search-insurance-claims-agent.ipynb)**  
    Develop a multi-agent insurance assistant for Hurricane damage to your property.

19. **[HR Recruitment Agent with Semantic Kernel](azure-ai-search-recruitment-agent)**  
    Automate HR candidate screening with a Semantic Kernel-driven agent.

## 🚀 Getting Started

To begin experimenting with these notebooks, set up your Azure AI environment with the following steps:

1. **Set Up an Azure Account**: Ensure you have an Azure account. If not, you can [sign up for free](https://azure.microsoft.com/free/).

2. **Create Azure AI Resources**: Follow the [Azure AI documentation](https://docs.microsoft.com/en-us/azure/cognitive-services/) to create the necessary resources, including Azure OpenAI service instances.

3. **Clone This Repository**: Clone the repository to your local machine or Azure Notebooks environment:

   ```bash
   git clone https://github.com/farzad528/azure-ai-search-python-playground.git
   ```

## 🛠️ Install Dependencies

Each notebook specifies its dependencies at the beginning. To ensure a smooth experience:

1. **Open the Notebook**: Navigate to the notebook of interest.

2. **Install Dependencies**: Follow the markdown instructions at the top of each notebook to install the necessary Python packages.

3. **Use a Virtual Environment (Recommended)**: It's highly recommended to use a virtual environment (via `conda`, `virtualenv`, or Python's built-in `venv` module) to avoid conflicts between project dependencies.

By following the in-notebook instructions, you can ensure that all necessary dependencies for a given experiment are correctly installed.

## 📚 How to Use

Each notebook is self-contained and includes step-by-step instructions to guide you through the experiments. To get started, simply open a notebook in your Jupyter environment and follow the provided instructions.

## 🤝 Contributing

We welcome contributions from the community! If you have suggestions for additional experiments or improvements to existing notebooks, please feel free to open an issue or submit a pull request.

## 🔔 Stay Updated

For more information and updates on using Azure AI for search and retrieval tasks, follow my blog on [Hashnode](https://hashnode.com/@Farzzy528).

Thank you for exploring the Azure AI Search Python Playground. Happy experimenting! 🎉