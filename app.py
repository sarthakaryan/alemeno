import streamlit as st
from streamlit_chat import message
from langchain.chains.question_answering import load_qa_chain
from langchain.chains.question_answering import load_qa_chain
from langchain.embeddings import HuggingFaceEmbeddings
from llama_index.embeddings.langchain import LangchainEmbedding
from llama_index.core import Settings
from llama_index.core import SimpleDirectoryReader
from langchain_community.llms import GPT4All
from langchain.schema import Document
from deeplake.core.vectorstore import VectorStore

@st.cache_resource
def initialize_chain():
    return load_qa_chain(GPT4All(model="./qwen2-0_5b-instruct-q8_0",), chain_type="stuff")

@st.cache_resource
def initialize_embed_model():
    return LangchainEmbedding(HuggingFaceEmbeddings(model_name="./sentence-transformers"))

@st.cache_resource
def initialize_vector_store():
    return VectorStore(path="dataset", read_only=True)

chain = initialize_chain()
embed_model = initialize_embed_model()
vector_store = initialize_vector_store()

def get_response(user_input):
    docs = vector_store.search(user_input,embedding_function=embed_model.get_text_embedding)
    docs = [Document(page_content=text) for text in docs]
    return chain.run(input_documents=docs, question=user_input)





st.title("Alemeno Bot 🤖")
if "messages" not in st.session_state:
    st.session_state.messages = []


with st.form(key="chat_form", clear_on_submit=True):
    placeholder = st.empty()
    user_input = st.text_input("You: ", "")
    submit_button = st.form_submit_button(label="Send")
    
if submit_button and user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        response = get_response(user_input.replace("?",""))
        st.session_state.messages.append({"role": "bot", "content": response})

with placeholder.container():
    for message_ in st.session_state.messages:
        if message_["role"] == "user":
            message(message_['content'],is_user=True)
        else :
            message(message_['content'])
