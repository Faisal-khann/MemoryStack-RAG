#read files
#break in chunks
#embeddings 
#store in vector store -> FAISS

import os
from langchain_community.document_loaders import (
    DirectoryLoader,
    PyPDFLoader,
    TextLoader
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# Root folder containing all knowledge documents (PDF + TXT)
DATA_PATH = "../knowledge_base"

# Folder where FAISS index + metadata will be persisted
FAISS_PATH = "../faiss_index"