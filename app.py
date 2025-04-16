import streamlit as st
from openai import OpenAI

# Set page title
st.set_page_config(page_title="Elite Fitness Center - AI Assistant")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Display title and intro
st.title("🤖 Elite Fitness Center - AI Assistant")
st.write("Welcome! Ask me anything about our gym, classes, or offers.")

# Handle chat input
if prompt := st.chat_input("Type your question here…"):
    st.chat_message("user").write(prompt)
    st.session_state.chat_history.append({"role": "user", "content": prompt})

    try:
        # Generate AI response
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

Answer all queries using only the above gym-specific information. If unsure, ask them to contact the front desk.
"""
                },
                *st.session_state.chat_history
            ]
        )

        answer = response.choices[0].message.content
        st.chat_message("assistant").write(answer)
        st.session_state.chat_history.append({"role": "assistant", "content": answer})

    except Exception as e:
        st.error("⚠️ Sorry, I ran into an issue. Please try again later.")
        st.exception(e)

# Show entire conversation
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
