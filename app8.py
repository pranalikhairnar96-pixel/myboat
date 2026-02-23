import streamlit as st
import google.generativeai as genai

# Page config
st.set_page_config(page_title="Pranali's AI Chatbot", page_icon="🤖")

st.title("🤖 Welcome to My GenAI Chatbot")

# Configure Gemini API
genai.configure(api_key="AIzaSyCSjK5o_HztbHaWyjZRSHUb5P7MXbybfxc")

model = genai.GenerativeModel("models/gemini-2.5-flash")

# Create chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input box (like ChatGPT)
prompt = st.chat_input("Ask me anything...")

if prompt:
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Save user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = model.generate_content(prompt)
            reply = response.text
            st.markdown(reply)

    # Save assistant response
    st.session_state.messages.append({"role": "assistant", "content": reply})

# Clear chat button
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()