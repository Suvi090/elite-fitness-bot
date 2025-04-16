import streamlit as st

st.set_page_config(page_title="Elite Fitness Center - AI Assistant", page_icon="🤖")

st.markdown("# 🤖 Elite Fitness Center - AI Assistant")
st.write("Welcome! I’m here to help you with info about our gym, martial arts classes, and offers.")

# Gym Details
with st.expander("🧘 Gym Details"):
    st.markdown("""
- ✅ **Semi-private gym sessions** with personal training at half the cost.
- 🕒 **Morning:** 5:30 AM – 10:30 AM | **Evening:** 4:30 PM – 10:30 PM
- 💪 Includes 3 weight training sessions + 3 cardio/kickboxing options weekly
- 💰 ₹1000 for a 1-week trial
""")

# Martial Arts
with st.expander("🥋 Martial Arts for Kids & Teens"):
    st.markdown("""
- Beginner-friendly martial arts
- Focus on discipline, fitness, and fun
- Separate timing slots for kids
""")

# MMA & Kickboxing
with st.expander("🥊 MMA & Kickboxing for Teens & Adults"):
    st.markdown("""
- Real MMA & Kickboxing training
- Learn proper technique, form, and conditioning
- Evening sessions available weekly
""")

# Location
with st.expander("📍 Location"):
    st.markdown("📌 Elite Fitness Center, Kochi, Kerala (Exact location sent via WhatsApp after booking)")

# Offers
with st.expander("🎁 Offers"):
    st.markdown("- 1 free martial arts class • ₹1000 1-week gym test")

# Chat Section
st.info("Want to book or ask a question? Just type it in the chat box below.")

user_input = st.chat_input("Type your question or message here...")

if user_input:
    st.write("👤 You asked:", user_input)

    if "time" in user_input.lower() or "timing" in user_input.lower():
        st.write("🕒 We’re open from 5:30 AM – 10:30 AM and 4:30 PM – 10:30 PM.")
    elif "price" in user_input.lower() or "cost" in user_input.lower() or "trial" in user_input.lower():
        st.write("💰 The 1-week gym trial is ₹1000. Martial arts trial is free!")
    elif "location" in user_input.lower():
        st.write("📍 We’re in Kochi, Kerala. Full location will be shared after booking.")
    else:
        st.write("🤖 Thanks for your message! We'll get back to you ASAP.")
