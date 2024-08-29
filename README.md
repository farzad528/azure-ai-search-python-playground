# Azure AI Search Python Playground

Welcome to the Azure AI Search Python Playground! This repository contains a collection of Jupyter notebooks that explore various capabilities of Azure AI Search, including vector search, retrieval-augmented generation (RAG), and other retrieval system tasks using OpenAI's embeddings models. Each notebook is designed as a standalone experiment and includes detailed explanations to help you understand the concepts and apply them in your own projects.

## Notebooks

Below is a list of the notebooks currently available in this repository:

1. [**Azure AI Search OpenAI Text-Embedding-3-Large Model Exploration**](azure-ai-search-text-embedding-3-large.ipynb) - This notebook demonstrates how to use the new OpenAI embeddings models within Azure AI Search. 
2. [**Azure AI Search Cohere Embed-v3 Exploration**](azure-ai-search-cohere-embed-v3.ipynb) - Explore the capabilities of the Cohere Embed-v3 model with Azure AI Search.
3. [**Azure AI Search with CSV Data**](azure-ai-search-csv.ipynb) - Utilize CSV data in Azure AI Search for indexing and querying.
4. [**Azure AI Search Document Boosting**](azure-ai-search-document-boosting.ipynb) - Learn techniques for boosting document relevance in Azure AI Search.
5. [**Azure AI Search RAG Evaluation with Tonic AI**](azure-ai-search-rag-eval-tonic-ai.ipynb) - Evaluate Retrieval-Augmented Generation (RAG) systems using Tonic AI Validate.
6. [**Azure AI Search RAG Evaluation with TruLens**](azure-ai-search-rag-eval-trulens.ipynb) - Evaluate RAG systems using the TruLens framework.
7. [**Azure AI Search Scalar Quantization**](azure-ai-search-scalar-quantization.ipynb) - Implement scalar quantization techniques in Azure AI Search to optimize performance.
8. [**Azure AI Search Llamaindex Workflows**](azure-ai-search-llamaindex-workflows.ipynb) - This notebook provides an in-depth exploration of creating workflows using the LlamaIndex framework. It demonstrates how to build event-driven, asynchronous workflows for tasks like RAG using Azure AI Search and OpenAI models.
9. [**Azure AI Search RAG Evaluation with Arize Phoenix**](azure-ai-search-rag-eval-arize-ai.ipynb) - Evaluate Retrieval-Augmented Generation (RAG) systems using Arize Phoenix AI
10.[**Azure AI Search Legal AI Agent with CrewAI**](azure-ai-search-crewai.ipynb) - Build a CrewAI Agent for a complex Legal AI Scenario using Azure AI Search, Azure OpenAI, and LlamaIndex.
11.[**Azure AI Search NVIDIA RAG w/LLamaIndex**](azure-ai-search-nvidia-rag.ipynb) - Build a RAG system using Azure AI Search, NVIDIA NIM hosted APIs for Embeddings and LLMs, orchestrated via LlamaIndex.


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
