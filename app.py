import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()
AZURE_OPENAI_API_KEY = os.getenv('AZURE_OPENAI_API_KEY')
AZURE_OPENAI_ENDPOINT = os.getenv('AZURE_OPENAI_ENDPOINT')
AZURE_OPENAI_DEPLOYMENT = os.getenv('AZURE_OPENAI_DEPLOYMENT')

openai.api_type = "azure"
openai.api_key = AZURE_OPENAI_API_KEY
openai.api_base = AZURE_OPENAI_ENDPOINT
openai.api_version = "2023-03-15-preview"

st.set_page_config(page_title="GPT-4.1 聊天问答", page_icon="💬")
st.title("GPT-4.1 聊天问答")

if 'messages' not in st.session_state:
    st.session_state['messages'] = []

for msg in st.session_state['messages']:
    st.chat_message(msg['role']).write(msg['content'])

user_input = st.chat_input("请输入您的问题...")
if user_input:
    st.session_state['messages'].append({"role": "user", "content": user_input})
    with st.spinner("GPT-4.1 正在思考..."):
        response = openai.ChatCompletion.create(
            engine=AZURE_OPENAI_DEPLOYMENT,
            messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state['messages']]
        )
        answer = response.choices[0].message.content
        st.session_state['messages'].append({"role": "assistant", "content": answer})
        st.chat_message("assistant").write(answer)
