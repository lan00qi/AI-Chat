import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv
from st_chat_message import message

load_dotenv()
client = OpenAI(api_key=os.getenv("API_KEY"))

system_prompt = "You are an ai and you will be trying to communicate with a user. You are a very stiff person and difficult. "
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = [
    {"role": "system","content": system_prompt},
    
    ]

for chat in st.session_state["chat_history"]:
    if chat["role"] == "assistant":
        message(chat["content"])
    elif chat["role"] == "user":
        message(chat["content"], is_user = True )
    
        

with st.form("chat"):
    user_messages = st.text_input("Message")
    submitted = st.form_submit_button("send")
    if submitted and user_messages:
        st.session_state["chat_history"].append({"role":"user","content": user_messages})
        response = client.chat.completions.create(
            model = "gpt-3.5-turbo-0125",
            messages = st.session_state["chat_history"]
        
            
        )
        st.session_state["chat_history"].append({"role":"assistant","content": response.choices[0].message.content})



