import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_mistralai.embeddings import MistralAIEmbeddings
from mistralai import Mistral
import faiss
from dotenv import load_dotenv
import tempfile
import os

load_dotenv()

#load api keys
api_key = os.getenv("MISTRAL_API_KEY")

llm = Mistral(api_key=api_key)

embeddings = MistralAIEmbeddings(api_key=api_key,
                                 model="mistral-embed")

#app title
st.title("Personal RAG APP")

#file uploader
uploaded_file = st.sidebar.file_uploader('upload your file', type=['docx', 'pdf', 'txt'])

if uploaded_file is not None:
    temp_dir = tempfile.TemporaryDirectory()
    
    temp_file_path = os.path.join(temp_dir.name, uploaded_file.name)
    
    with open(temp_file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.success(f"File saved to temporary directory: {temp_file_path}")


    #read the pdf
    loader = PyPDFLoader(temp_file_path)

    document = loader.load()
    st.success("Document loaded successfully")
    if st.sidebar.button("Create Vector Store"):
        
        #create vector store
        st.success("Button working fine")
    