import streamlit as st

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

# Sidebar
with st.sidebar:
    st.title("⚙️ Settings")
    if st.button("Clear Chat"):
        st.session_state.messages = []

# Title
st.title("🤖 AI Chatbot")

# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input
user_input = st.chat_input("Type your message...")

# Improved smart reply
def bot_reply(user_text):
    user_text = user_text.lower()

    if any(word in user_text for word in ["hi", "hello", "hey", "hii"]):
        return "Heyy! 😊 How can I help you today?"
    
    elif "how are you" in user_text:
        return "I'm doing great! What about you?"
    
    elif "python" in user_text:
        return "Python is amazing 🐍 What do you want to build?"
    
    elif "project" in user_text:
        return "You can build AI chatbot, resume parser, or ML models 🚀"
    
    elif "bye" in user_text:
        return "Bye! Take care 💫"
    
    else:
        return "I'm still learning 🤖 Try asking about Python, projects, or greetings!"

# Chat logic
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    reply = bot_reply(user_input)

    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.write(reply)