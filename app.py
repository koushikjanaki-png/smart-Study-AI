import streamlit as st
import openai

# -------------------------------
# SmartStudy AI – NCERT & State Board
# -------------------------------

# Replace this with your OpenAI API key
openai(api_key = "YOUR_API_KEY")

# Streamlit page configuration
st.set_page_config(page_title="SmartStudy AI", page_icon="📚")

# App title and description
st.title("📚 SmartStudy AI")
st.write("Ask questions from your 9th grade syllabus (NCERT & State Board).")

# Dropdown to select syllabus
book_option = st.selectbox(
    "Select Book:", 
    ["NCERT", "State Board", "Both"]
)

# Text input for the user's question
user_question = st.text_input("Enter your question:")

# Button to get AI answer
if st.button("Get Answer"):
    if user_question:  # Ensure question is not empty
        with st.spinner("Fetching answer..."):
            try:
                # System prompt depending on syllabus selection
                if book_option == "NCERT":
                    system_prompt = "You are a 9th grade teacher. Answer questions using the NCERT syllabus only."
                elif book_option == "State Board":
                    system_prompt = "You are a 9th grade teacher. Answer questions using the State Board syllabus only."
                else:
                    system_prompt = "You are a 9th grade teacher. Answer questions using both NCERT and State Board syllabus."

                # Call OpenAI API to get the answer
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_question}
                    ],
                    max_tokens=600
                )

                # Display the answer
                answer = response['choices'][0]['message']['content']
                st.success(answer)

            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a question.")
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_input}
    ]
)
reply = response.choices[0].message["content"]
st.write(reply)
