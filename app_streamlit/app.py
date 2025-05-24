import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
import tempfile
import os


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
    path = str(temp_file_path)
    loader = PyPDFLoader(temp_file_path)

    document = loader.load()

    st.write(document[0])