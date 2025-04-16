
import streamlit as st

st.set_page_config(page_title="Elite Fitness Center AI Assistant", layout="centered")

st.title("🤖 Elite Fitness Center - AI Assistant")
st.write("Welcome! I’m here to help you with info about our gym, martial arts classes, and offers.")

with st.expander("🏋️ Gym Details"):
    st.write("""
    - ✅ Semi-private gym sessions with personal training at half the cost.
    - 🕔 Morning: 5:30 AM – 10:30 AM | Evening: 4:30 PM – 10:30 PM
    - 💪 Includes 3 weight training sessions + 3 cardio/kickboxing options weekly
    - 💰 ₹1000 for a 1-week trial
    """)

with st.expander("🥋 Martial Arts for Kids & Teens"):
    st.write("""
    - Karate, Taekwondo, Kung Fu (Wushu) – for kids under 13
    - Classes: 2/week | Morning 6–10 AM, Evening 4–9 PM
    """)

with st.expander("🥊 MMA & Kickboxing for Teens & Adults"):
    st.write("""
    - For ages 13+ | Unisex
    - 🥊 Kickboxing: Tue, Thu, Sat (7–10 AM), Mon–Sat (4–10 PM)
    - 🧩 MMA: Mon–Sat (4–10 PM)
    - 🤼 Wrestling: Sunday only – 2 classes
    """)

with st.expander("📍 Location"):
    st.markdown("[📌 Find us on Google Maps](https://g.co/kgs/QZsRoS3)")

with st.expander("🎁 Offers"):
    st.write("🥋 1 free martial arts class • ₹1000 1-week gym test")

st.infost.info("Want to book or ask a question? Just type it in the chat box below.")

        import streamlit as st

# Chat input at the bottom of the app
user_input = st.chat_input("Type your question or message here...")

# Basic display of the message
if user_input:
    st.write("👤 You asked:", user_input)
    # Optionally add logic to respond to common queries
    if "timing" in user_input.lower():
        st.write("🕒 We’re open from 5:30 AM – 10:30 AM and 4:30 PM – 10:30 PM.")
    elif "price" in user_input.lower() or "cost" in user_input.lower():
        st.write("💰 The 1-week gym trial is ₹1000 including 6 sessions.")
    else:
        st.write("🤖 Thanks for your message! We'll get back to you soon.")
