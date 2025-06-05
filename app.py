
import streamlit as st
from duckduckgo_search import DDGS

st.title("DuckDuckGo Search Agent")
st.write("Enter a query below and get search results from DuckDuckGo.")

query = st.text_input("Your Search Query:")

if st.button("Search") and query:
    st.write(f"Searching DuckDuckGo for: '{query}'")

    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=5)
        for idx, r in enumerate(results, start=1):
            st.markdown(f"**{idx}. [{r['title']}]({r['href']})**")
            st.write(r['body'])
