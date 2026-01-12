import streamlit as st
from dotenv import load_dotenv
from agent.agent_executor import create_agent

load_dotenv()

st.set_page_config(page_title="Travel Booking AI Agent", page_icon="✈️")

st.title("✈️ Travel Booking AI Agent")
st.subheader("BCA Final Year Project using LangChain & Python")

agent = create_agent()

if "chat" not in st.session_state:
    st.session_state.chat = []

user_input = st.text_input("Ask about travel plans:")

if user_input:
    response = agent.run(user_input)
    st.session_state.chat.append(("You", user_input))
    st.session_state.chat.append(("AI Agent", response))

for role, msg in st.session_state.chat:
    st.markdown(f"**{role}:** {msg}")
