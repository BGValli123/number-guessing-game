import streamlit as st
import random

st.set_page_config(page_title="Number Guessing Game")

st.title("🎯 Number Guessing Game")

# Initialize session state
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

# Input
guess = st.number_input("Enter your guess (1-100):", min_value=1, max_value=100)

# Button
if st.button("Check Guess") and not st.session_state.game_over:
    st.session_state.attempts += 1

    if guess == st.session_state.number:
        st.success(f"🎉 Correct! You guessed it in {st.session_state.attempts} attempts.")
        st.session_state.game_over = True

    elif guess > st.session_state.number:
        st.warning("📉 Too High!")

    else:
        st.warning("📈 Too Low!")

# Restart button
if st.session_state.game_over:
    if st.button("Play Again"):
        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.experimental_rerun()