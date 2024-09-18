import streamlit as st
from GroqZeroShot import groq_prompt


def paraphrase_process(text):
   
    paraphrase_response = groq_prompt(text)
    st.write(paraphrase_response)
    
st.title("🦙💬 Alfred")
st.caption("🚀 A Custom Paraphase Generator")

with st.container(border=True):
    
    text = st.text_area('What do you want to paraphrase?')
    button = st.button('Paraphrase')

    with st.spinner("Paraphrasing.."):
        if text and button:
            paraphrase_process(text)