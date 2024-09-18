import streamlit as st
from TransformerParaphraser import paraphrase


def paraphrase_process(text):

    text_length = len(text)
    paraphrase_response = paraphrase(text, text_length)
    for i, paraphrases in enumerate(paraphrase_response, 1):
        st.write(f"{i}. {paraphrases}")
    
st.title("🦙💬 Alfred")
st.caption("🚀 A Custom Paraphase Generator")

with st.container(border=True):
    
    text = st.text_area('What do you want to paraphrase?')
    button = st.button('Paraphrase')

    with st.spinner("Paraphrasing.."):
        if text and button:
            paraphrase_process(text)