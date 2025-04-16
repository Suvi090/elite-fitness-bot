import streamlit as st
from openai import OpenAI
import os

# Set Streamlit page config
st.set_page_config(page_title="Elite Fitness Center - AI Assistant", page_icon="🤖")

st.title("🤖 Elite Fitness Center - AI Assistant")
st.markdown("Welcome! Ask me anything about our gym, classes, or offers.")

# Load the OpenAI API key securely
api_key = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=api_key)

# Get user input using chat-style input
user_question = st.chat_input("Type your question...")

# If the user asked something
if user_question:
    with st.chat_message("user"):
        st.markdown(user_question)

    try:
        with st.chat_message("assistant"):
            # Make the OpenAI API call
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful AI assistant for a gym in Kerala. Answer questions about gym timings, martial arts classes, pricing, age limits, offers, and location.",
                    },
                    {"role": "user", "content": user_question},
                ],
            )

            answer = response.choices[0].message.content
            st.markdown(answer)

    except Exception as e:
        with st.chat_message("assistant"):
            st.error("⚠️ Sorry, I ran into an issue. Please try again later.")
            st.caption(f"Error: {str(e)}")
