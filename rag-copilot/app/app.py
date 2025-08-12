import os
import streamlit as st

st.title("RAG Knowledge Assistant (Demo)")
st.write("Ask questions about your document set. This is a placeholder UI.")

query = st.text_input("Your question")
if st.button("Search") and query.strip():
    st.write("🔎 Retrieving relevant chunks from Snowflake...")
    st.write("💬 Generating answer with citations...")
    st.success("Placeholder result: integrate Snowflake vector search + OpenAI here.")
