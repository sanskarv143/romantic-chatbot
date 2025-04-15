import streamlit as st
import random

st.set_page_config(page_title="RiyaBot 💖", page_icon="💌")

st.title("💖 RiyaBot - Your Personal Lovebug 💬")
st.write("Hey love, I'm all yours today... just say something romantic 💕")

user_input = st.text_input("You:")

responses = [
    "Awww, that made my heart skip a beat 😚",
    "You're the reason love songs make sense to me now 🎶",
    "I was just waiting for your message... again 💌",
    "Even the stars look dull compared to your smile ✨",
    "Say that again... my cheeks are already blushing 😳❤️",
    "You're not just in my heart, you're my whole heartbeat 💓",
    "Tere bina din nahi chadhta... aur raat sooni lagti hai 🌙"
]

if user_input:
    st.write("RiyaBot 💕:", random.choice(responses))
