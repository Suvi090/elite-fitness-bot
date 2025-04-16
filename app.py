import streamlit as st
from openai import OpenAI

# Load OpenAI API key from Streamlit secrets (or manually set here)
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Page settings
st.set_page_config(page_title="Elite Fitness Center - AI Assistant", page_icon="🤖")

# System instructions (gym info)
SYSTEM_PROMPT = """
You are a helpful assistant for Elite Fitness Center. You provide accurate answers about our gym services, timings, martial arts programs, and offers.

Here is the gym information:

✅ Semi-private gym sessions with personal training at half the cost  
🕒 Morning: 5:30 AM – 10:30 AM | Evening: 4:30 PM – 10:30 PM  
🏋️ Includes 3 weight training sessions + 3 cardio/kickboxing options weekly  
💰 ₹1000 for a 1-week trial  
🥋 Martial arts for kids, teens, and adults  
🎯 1 free martial arts class • ₹1000 1-week gym test  
📍 Location: Kochi
"""

# Initialize chat session
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": SYSTEM_PROMPT}]

# Title and intro
st.title("🤖 Elite Fitness Center - AI Assistant")
st.write("Welcome! Ask me anything about our gym, classes, or offers.")

# Display past conversation
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Get user input
if prompt := st.chat_input("Ask your question here..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        msg_placeholder = st.empty()
        msg_placeholder.markdown("🤔 Thinking...")

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=st.session_state.messages
            )
            reply = response.choices[0].message.content.strip()
        except Exception as e:
            reply = "⚠️ Sorry, I ran into an issue. Please try again later."

        msg_placeholder.markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})
