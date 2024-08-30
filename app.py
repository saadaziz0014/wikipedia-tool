from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import WikipediaQueryRun
import streamlit as st

st.title("Wikipedia Search")

wikipedia = WikipediaAPIWrapper()
wikipedia_query = WikipediaQueryRun(api_wrapper=wikipedia)

query = st.text_input("Enter a query:")

# on enter key press, run the query
if query:
    with st.spinner('Searching...'):
        result = wikipedia_query.invoke({"query": query})
        st.write(result)