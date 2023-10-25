import time
import streamlit as st
from main import *

st.set_page_config(page_title="Chatbot PDF", page_icon="🤖")
st.title("🤖 Chatbot PDF")
st.caption('¡Hola! Bienvenido al chatbot PDF')
st.session_state.conversation = qa

if 'history' not in st.session_state:
    st.session_state['history'] = []

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if 'disabled' not in st.session_state:
    st.session_state.disabled = False

if prompt := st.chat_input("¿En que te puedo ayudar?"):
    st.chat_input("Se está generando la respuesta, por favor espere...", key="disabled_chat_input", disabled=True)
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        with st.spinner('🧠 Pensando...'):
            result = qa({"question": prompt, "chat_history": st.session_state['history']})
            assistant_response = result["answer"].replace('$', ' $ ')
        for chunk in assistant_response.split(' '):
            full_response += chunk + " "
            time.sleep(0.05)
            message_placeholder.markdown(full_response + "|")
            message_placeholder.markdown(full_response)
        st.session_state['history'].append((prompt, result["answer"]))
        st.session_state.messages.append({"role": "assistant", "content": result["answer"]})
        st.experimental_rerun()
