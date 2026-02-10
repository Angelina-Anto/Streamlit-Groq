import streamlit as st
from sep2 import get_ai_response

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 AI Chatbot (Groq + Streamlit)")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Ask something...")

if user_input:
    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get AI response
    ai_response = get_ai_response(user_input)

    # Show assistant message
    st.session_state.messages.append(
        {"role": "assistant", "content": ai_response}
    )
    with st.chat_message("assistant"):
        st.markdown(ai_response)
