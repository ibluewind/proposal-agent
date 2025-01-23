import os
from typing import List
from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader,
    TextLoader,
    UnstructuredPowerPointLoader,
    UnstructuredExcelLoader
)
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings
from agent.config import VECTORSTORE_DIR, create_directories

from dotenv import load_dotenv

class DocumentProcessor:
    def __init__(self):
        self.loader_map = {
            '.pdf': PyPDFLoader,
            '.docx': Docx2txtLoader,
            '.txt': TextLoader,
            '.pptx': UnstructuredPowerPointLoader,
            '.xlsx': UnstructuredExcelLoader,
            '.xls': UnstructuredExcelLoader
        }
        
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        
        self.embeddings = OpenAIEmbeddings()
    
    def load_documents(self) -> List:
        """모든 문서를 로드하고 청크로 분할"""
        documents = []
        docs_dir = VECTORSTORE_DIR['documents']
        
        for filename in os.listdir(docs_dir):
            file_path = os.path.join(docs_dir, filename)
            file_extension = os.path.splitext(filename)[1].lower()
            
            if file_extension in self.loader_map:
                try:
                    loader = self.loader_map[file_extension](file_path)
                    documents.extend(loader.load())
                    print(f"Successfully loaded: {filename}")
                except Exception as e:
                    print(f"Error loading {filename}: {str(e)}")
            else:
                print(f"Unsupported file type: {filename}")
        
        return self.text_splitter.split_documents(documents)

def create_vectorstore():
    """Chroma vectorstore 생성"""
    create_directories()
    
    processor = DocumentProcessor()
    documents = processor.load_documents()
    
    if not documents:
        print("No documents were loaded. Please check the documents folder.")
        return
    
    # Chroma vectorstore 생성
    vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=processor.embeddings,
        persist_directory=VECTORSTORE_DIR['db'],
        collection_name="proposal_db"
    )
    
    # 저장
    vectorstore.persist()
    print(f"Vectorstore created successfully at {VECTORSTORE_DIR['db']}")
    return vectorstore

if __name__ == "__main__":
    load_dotenv()
    create_vectorstore()
