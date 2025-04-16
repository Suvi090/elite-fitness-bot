import streamlit as st
import openai
import os

# Set OpenAI API key from secret
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Elite Fitness Center - AI Assistant")

st.title("🤖 Elite Fitness Center - AI Assistant")

st.write("Welcome! I’m here to help you with info about our gym, martial arts classes, and offers.")

# Gym Details
with st.expander("🧾 Gym Details"):
    st.markdown("""
- ✅ **Semi-private gym sessions** with personal training at half the cost.  
- 🕒 **Morning:** 5:30 AM – 10:30 AM | **Evening:** 4:30 PM – 10:30 PM  
- 🏋️ Includes **3 weight training sessions + 3 cardio/kickboxing options weekly**  
- 💰 ₹1000 for a 1-week trial  
    """)

# Martial Arts
with st.expander("🥋 Martial Arts for Kids & Teens"):
    st.write("Special kids martial arts classes on weekends and evenings.")

with st.expander("🥊 MMA & Kickboxing for Teens & Adults"):
    st.write("Evening and weekend batches available. Great for fitness and self-defense.")

# Location
with st.expander("📍 Location"):
    st.write("Elite Fitness Center, Kochi")

# Offers
with st.expander("🎁 Offers"):
    st.write("1 free martial arts class • ₹1000 1-week gym test")

st.divider()

# AI Chat Section
st.subheader("💬 Got a question? Ask me below!")

user_input = st.text_input("Type your question:")

if user_input:
    with st.spinner("Thinking..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant for a fitness center in Kerala. Answer questions about gym, timings, classes, offers, etc."},
                    {"role": "user", "content": user_input}
                ]
            )
            st.success(response['choices'][0]['message']['content'])
        except Exception as e:
            st.error(f"Something went wrong: {e}")
