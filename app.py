import streamlit as st
from streamlit_chat import message

from langchain.embeddings import HuggingFaceEmbeddings
from llama_index.embeddings.langchain import LangchainEmbedding
from langchain_community.llms import GPT4All
from langchain.schema import Document
from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.vector_stores.deeplake import DeepLakeVectorStore

@st.cache_resource
def initialize_llm():
    return GPT4All(model="./qwen2-0_5b-instruct-q8_0",)

@st.cache_resource
def initialize_embed_model():
    return LangchainEmbedding(HuggingFaceEmbeddings(model_name="./sentence-transformers"))

@st.cache_resource
def initialize_query_engine():
    vector_store = DeepLakeVectorStore(dataset_path="suni-dataset",read_only=True,)
    index = VectorStoreIndex.from_vector_store(vector_store=vector_store,embed_model=embed_model)
    return index.as_query_engine(llm=llm)

llm = initialize_llm()
embed_model = initialize_embed_model()
query_engine = initialize_query_engine()

def get_response(user_input):
    return query_engine.query(user_input).response



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
