import os
from dotenv import load_dotenv

from langchain.document_loaders import (
    ReadTheDocsLoader,
)  # helps build documentation for GitHub repo
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
import pinecone


load_dotenv()

pinecone.init(
    api_key=os.environ["PINECONE_API_KEY"],
    environment=os.environ["PINECONE_ENVIRONMENT_REGION"],
)


def ingest_docs() -> None:
    loader = ReadTheDocsLoader(
        path="/Users/morgan/Documents/04_Online_Courses/13_udemy_langchain/langchain-apps-v2/langchain-docs/api.python.langchain.com/en/latest"
    )
    raw_documents = loader.load()
    print(f"Loaded {len(raw_documents)} documents")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=400, chunk_overlap=50, separators=["\n\n", "\n", " ", ""]
    )
    documents = text_splitter.split_documents(documents=raw_documents)
    print(f"Splitted into {len(documents)} chunks")

    for doc in documents:
        old_path = doc.metadata["source"]
        new_url = old_path.replace("langchain-docs", "https:/")
        doc.metadata.update({"source": new_url})

    print(f"Going to insert {len(documents)} to Pinecone")
    embeddings = OpenAIEmbeddings()
    Pinecone.from_documents(documents, embeddings, index_name=INDEX_NAME)
    print("****** Added to Pinecone vectorstore vectors")


if __name__ == "__main__":
    ingest_docs()
