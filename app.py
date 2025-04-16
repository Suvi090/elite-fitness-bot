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
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": """
You are an AI assistant for Elite Fitness Center in Kerala.
Here are the gym's actual policies and offerings:

- Age limit to join gym: Minimum age is 16 with parental consent, 18+ without.
- Gym timings: Morning 5:30 AM – 10:30 AM | Evening 4:30 PM – 10:30 PM
- Offers: ₹1000 for a 1-week trial, includes 3 weight training + 3 cardio/kickboxing sessions.
- Martial Arts: Classes available for both kids and adults, including MMA and Kickboxing.

Answer all queries only using the above gym-specific information. If unsure, ask them to contact the front desk.
"""
        },
        *st.session_state.chat_history
    ]
)

        ai_reply = response.choices[0].message.content.strip()

    except Exception as e:
        ai_reply = f"⚠️ Sorry, I ran into an issue. Please try again later.\n\nError: {str(e)}"

    # Display assistant response and save it
    with st.chat_message("assistant"):
        st.markdown(ai_reply)
    st.session_state.chat_history.append({"role": "assistant", "content": ai_reply})
