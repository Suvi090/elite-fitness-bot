import streamlit as st
from openai import OpenAI
import os

# Initialize the OpenAI client using the secret from Streamlit settings
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# App title and intro
st.set_page_config(page_title="Elite Fitness Center - AI Assistant")
st.title("🤖 Elite Fitness Center - AI Assistant")
st.markdown("Welcome! Ask me anything about our gym, classes, or offers.")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_query = st.chat_input("Type your question here...")

if user_query:
    # Display user message and save it
    with st.chat_message("user"):
        st.markdown(user_query)
    st.session_state.chat_history.append({"role": "user", "content": user_query})

    # Process user query via OpenAI
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # You can switch to gpt-4 if needed
            messages=st.session_state.chat_history
        )
        ai_reply = response.choices[0].message.content.strip()

    except Exception as e:
        ai_reply = f"⚠️ Sorry, I ran into an issue. Please try again later.\n\nError: {str(e)}"

    # Display assistant response and save it
    with st.chat_message("assistant"):
        st.markdown(ai_reply)
    st.session_state.chat_history.append({"role": "assistant", "content": ai_reply})
