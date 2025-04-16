import streamlit as st
from openai import OpenAI
import os

st.set_page_config(page_title="Elite Fitness Chatbot 💪", layout="centered")

# Set up OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Title and instructions
st.title("🤖 Elite Fitness Center - AI Assistant")
st.write("Ask me anything about the gym, classes, timings, or offers!")

# Use chat input at the bottom of the page
user_input = st.chat_input("Type your question here...")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an AI assistant for a fitness center. Answer clearly and helpfully."},
                    {"role": "user", "content": user_input}
                ]
            )
            st.write(response.choices[0].message.content)
