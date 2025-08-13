from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()


GEMINI_API = os.getenv("GOOGLE_API_KEY")

#prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("user", "Question:{question}")
    ]
)

#streamlit framework
st.title("Chatbot")
st.write("Ask a question:")
question = st.text_input("Question:")

#gemini llm
llm= ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    api_key=GEMINI_API
)

output_parser = StrOutputParser()
chain=prompt | llm | output_parser

if question:
    with st.spinner("Generating response..."):
        try:
            response = chain.invoke({"question": question})
            st.write("Response:", response)
        except Exception as e:
            st.error(f"An error occurred: {e}")