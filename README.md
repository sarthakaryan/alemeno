# Alemeno Bot 🤖

## Overview
Alemeno Bot is a Streamlit-based chatbot application that integrates question answering and conversational capabilities using Langchain and HuggingFace embeddings.

![Screenshot 2024-07-06 022023](https://github.com/sarthakaryan/alemeno/assets/32753858/5b31698e-481d-41ae-9ebc-d10373646938)


## Installation
To run the Alemeno Bot locally, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install dependencies:
   ```
   pip install streamlit
   pip install langchain
   pip install langchain_community
   pip install llama_index
   pip install deeplake
   pip install llama-index-embeddings-langchain
   pip install gpt4all
   pip install llama-index-vector-stores-deeplake
   pip install sentence-transformers
   pip install llama-index-llms-langchain
   pip install llama_index.llms.fireworks
   ```

3. Ensure required data and models are accessible:
   - Download and place your dataset in the `dataset` directory for vector storage.
   - Ensure model paths (`./qwen2-0_5b-instruct-q8_0` and `./sentence-transformers`) are correctly configured in the script.

## Usage
1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

2. Interact with Alemeno Bot in your browser:
   - Enter your query in the text input field labeled "You:" and click "Send".
   - Alemeno Bot will respond with relevant information based on the query.

## Components
- **Streamlit Interface**: Provides a user-friendly chat interface.
- **Langchain Question Answering Chain**: Utilizes GPT4All model for question answering.
- **HuggingFace Embeddings**: Handles text embeddings using the SentenceTransformers model.
- **VectorStore**: Manages vector storage and retrieval from the dataset.

## Credits
- Developed by Sarthak Aryan
- Powered by [Langchain](https://langchain.com) and [HuggingFace](https://huggingface.co)

---

This approach consolidates the installation instructions with the dependencies directly listed, making it convenient for users to set up your project environment. Adjust the URLs, credits, and other details as per your project specifics.
