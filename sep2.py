import streamlit as st
from groq import Groq

# Create Groq client using Streamlit Secrets
client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

def get_ai_response(user_message):
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": user_message}
        ],
        model="llama-3.3-70b-versatile",
    )

    return chat_completion.choices[0].message.content
