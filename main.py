from typing import Set

from backend.core import run_llm
import streamlit as st
from streamlit_chat import message

st.header("LangChain Udemy Course - Documentation Helper Bot")


prompt = st.text_input("Prompt", placeholder="Enter your prompt here...")

"""
Streamlit Notes:
----------------
- Everytime a user interacts with a Streamlit app, the entire script is reran.
- As such, any data generated or modified during the script run will be lost.
- Session state allows data to be stored/persisted across reruns

"""


def create_sources_string(source_urls: Set[str]) -> str:
    if not source_urls:
        return ""
    sources_list = list(source_urls)
    sources_list.sort()
    sources_string = "sources:\n"
    for i, source in enumerate(sources_list):
        sources_string += f"{i+1}. {source}\n"
    return sources_string


if prompt:
    with st.spinner("Generating response..."):
        generate_response = run_llm(query=prompt)
        sources = set(
            [doc.metadata["source"] for doc in generate_response["source_documents"]]
        )

        formatted_response = (
            f"{generate_response['result']} \n\n {create_sources_string(sources)}"
        )
