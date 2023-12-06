import os
from dotenv import load_dotenv

from langchain.document_loaders import ReadTheDocsLoader # helps build documentation for GitHub repo


def ingest_docs() -> None:
    loader = ReadTheDocsLoader(path="/Users/morgan/Documents/04_Online_Courses/13_udemy_langchain/langchain-apps-v2/langchain-docs/api.python.langchain.com/en/latest")


if __name__ == "__main__":
    ingest_docs()