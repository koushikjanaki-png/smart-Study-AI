# app.py
import streamlit as st
import openai
import os

# -----------------------------
# 1. Set OpenAI API key
# -----------------------------
openai.api_key = os.getenv("OPENAI_API_KEY")

# -----------------------------
# 2. Streamlit UI Setup
# -----------------------------
st.set_page_config(page_title="Smart Study AI - NCERT + State Board 9th", page_icon="📚", layout="centered")
st.title("Smart Study AI - 9th NCERT & State Board 📖")
st.markdown("Ask questions related to 9th-grade NCERT and State Board textbooks (Science, Math, Social Science, English).")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
user_input = st.text_input("Your question:")

# -----------------------------
# 3. Chat Submission
# -----------------------------
if st.button("Submit") and user_input.strip() != "":
    # Save user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("Thinking... 🤔"):
        try:
            # AI call with NCERT + State Board instructions
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", 
                     "content": (
                        "You are a helpful study assistant. Only provide answers according to the "
                        "9th-grade NCERT and State Board textbooks (Science, Math, Social Science, English). "
                        "Do not provide information outside these textbooks unless explicitly asked."
                     )},
                    *st.session_state.messages  # Include chat history
                ]
            )

            answer = response.choices[0].message.content

            # Save AI response
            st.session_state.messages.append({"role": "assistant", "content": answer})

        except Exception as e:
            st.error(f"Error: {e}")

# -----------------------------
# 4. Display Chat History
# -----------------------------
for chat in st.session_state.messages:
    if chat["role"] == "user":
        st.markdown(f"**You:** {chat['content']}")
    else:
        st.markdown(f"**AI:** {chat['content']}")
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ]
)

print(response.choices[0].message.content)
