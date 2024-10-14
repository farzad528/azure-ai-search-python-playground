# Azure AI Search Python Playground

Welcome to the Azure AI Search Python Playground! This repository contains a collection of Jupyter notebooks that explore various capabilities of Azure AI Search, including vector search, retrieval-augmented generation (RAG), and other retrieval system tasks using OpenAI's embeddings models. Each notebook is designed as a standalone experiment and includes detailed explanations to help you understand the concepts and apply them in your own projects.

## Notebooks

This repository contains a collection of Jupyter notebooks that demonstrate various integrations and functionalities using Azure AI Search and related technologies.

1. **[Azure AI Search OpenAI Text-Embedding-3-Large Model Exploration](azure-ai-search-text-embedding-3-large.ipynb)**  
   Integrates OpenAI's text-embedding-3-large model with Azure AI Search for enhanced search capabilities.

2. **[Azure AI Search Cohere Embed-v3 Exploration](azure-ai-search-cohere-embed-v3.ipynb)**  
   Explores the Cohere Embed-v3 model within Azure AI Search to improve embedding performance.

3. **[Azure AI Search with CSV Data](azure-ai-search-csv.ipynb)**  
   Demonstrates how to index and query CSV data using Azure AI Search.

4. **[Azure AI Search Document Boosting](azure-ai-search-document-boosting.ipynb)**  
   Techniques for enhancing document relevance and search ranking in Azure AI Search.

5. **[Azure AI Search RAG Evaluation with Tonic AI](azure-ai-search-rag-eval-tonic-ai.ipynb)**  
   Evaluates Retrieval-Augmented Generation (RAG) systems using Tonic AI Validate.

6. **[Azure AI Search RAG Evaluation with TruLens](azure-ai-search-rag-eval-trulens.ipynb)**  
   Assesses RAG systems leveraging the TruLens framework for improved evaluation.

7. **[Azure AI Search Scalar Quantization](azure-ai-search-scalar-quantization.ipynb)**  
   Implements scalar quantization techniques to optimize Azure AI Search performance.

8. **[Azure AI Search LlamaIndex Workflows](azure-ai-search-llamaindex-workflows.ipynb)**  
   Builds event-driven, asynchronous workflows using the LlamaIndex framework with Azure AI Search and OpenAI models.

9. **[Azure AI Search RAG Evaluation with Arize Phoenix](azure-ai-search-rag-eval-arize-ai.ipynb)**  
   Evaluates RAG systems using Arize Phoenix AI for enhanced analytics.

10. **[Azure AI Search Legal AI Agent with CrewAI](azure-ai-search-legal-ai-agent.ipynb)**  
    Develops a CrewAI Agent for complex legal scenarios using Azure AI Search, Azure OpenAI, and LlamaIndex.

11. **[Azure AI Search NVIDIA RAG with LlamaIndex](azure-ai-search-nvidia-rag.ipynb)**  
    Constructs a RAG system integrating Azure AI Search, NVIDIA NIM APIs for embeddings and LLMs, orchestrated via LlamaIndex.

12. **[Azure AI Search Medical AI Agent with CrewAI](azure-ai-search-medical-ai-agent.ipynb)**  
    Builds a multi-agent medical decision support system for cardiology, generating personalized treatment recommendations based on guidelines using Azure AI Search, Azure OpenAI, LlamaIndex, LlamaParse, and CrewAI.
13. **[[NEW] Azure AI Search Multimodal RAG using Contextual Retrieval](azure-ai-search-contextual-retreival.ipynb)**  
    Build a multidmodal RAG query engine using LlamaParse Premium, Azure OpenAI, Azure AI Search, and Arize Phoenix with Contextual Retrieval. 


## Getting Started

To get started with these notebooks, you'll need to set up your Azure AI environment. Here's a quick guide:

1. **Set Up Azure Account**: Ensure you have an Azure account. If not, you can [sign up for free](https://azure.microsoft.com/free/).

2. **Create Azure AI Resources**: Follow the [Azure AI documentation](https://docs.microsoft.com/en-us/azure/cognitive-services/) to create the necessary resources, including Azure OpenAI service instances.

3. **Clone This Repository**: Clone this repository to your local machine or Azure Notebooks environment to get started with the experiments.

   ```bash
   git clone https://github.com/farzad528/azure-ai-search-python-playground.git
   ```

## Install Dependencies

Each notebook in this repository contains its specific dependency installations at the beginning of the notebook. To ensure a smooth experience:

1. **Open the Notebook**: Navigate to the notebook of interest.

2. **Install Dependencies**: Follow the markdown instructions provided at the top of each notebook to install necessary Python packages. This approach keeps each experiment self-contained and allows for flexibility in dependency versions across different notebooks.

3. **Virtual Environment (Recommended)**: While not required, it's highly recommended to use a virtual environment for running the notebooks to avoid potential conflicts between dependencies of different projects. This can be done using `conda`, `virtualenv`, or Python's built-in `venv` module.

By following the in-notebook instructions, you can ensure that all necessary dependencies for a given experiment are correctly installed and configured.


## How to Use

Each notebook in this repository is self-contained and includes step-by-step instructions to guide you through the experiments. To begin, simply open the notebook of interest in your Jupyter environment and follow along with the instructions provided within.

## Contributing

Your contributions are welcome! If you have suggestions for additional experiments or improvements to existing notebooks, please feel free to open an issue or submit a pull request.

## Stay Updated

For more information and updates on using Azure AI for search and retrieval tasks, follow my blog on [Hashnode](https://hashnode.com/@Farzzy528).

Thank you for exploring the Azure AI Search Python Playground. Happy experimenting!
