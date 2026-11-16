import os
import streamlit as st
from google import genai
from dotenv import load_dotenv
from google.genai import types
from prompt import SYSTEM_PROMPT

load_dotenv ()
api_key=os.getenv('GEMINI_API_KEY')


client = genai.Client(api_key=api_key)


st.title("Talk to Chatbot")
st.write("This app demonstrate a conversational agent.")

user_input=st.text_input("Ask a question")
if st.button("Submit"):
    with st.spinner("Agent is thinking..."):
        response = client.models.generate_content(
            model='gemini-3.8-flash', contents=user_input,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT
                )
        )
        
        st.write(response.text)