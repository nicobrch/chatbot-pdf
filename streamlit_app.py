import streamlit as st
import openai
import os
from dotenv import load_dotenv
from llama_index import VectorStoreIndex, ServiceContext
from llama_index.llms import OpenAI
from llama_index import SimpleDirectoryReader

load_dotenv()

st.set_page_config(page_title="OpenAI Chat", page_icon="🤖", layout="centered", initial_sidebar_state="auto",
                   menu_items=None)
openai.api_key = os.getenv("OPENAI_API_KEY")
st.title("🤖 Chatea usando tus documentos PDF")

if "messages" not in st.session_state.keys():  # Initialize the chat messages history
    st.session_state.messages = [
        {"role": "assistant", "content": "Hazme una pregunta!"}
    ]


def read_prompt():
    prompt_file: str = ""
    try:
        with open("prompt.txt", "r") as file:
            prompt_file = file.read()
    except FileNotFoundError:
        print(f"No existe el archivo prompt.txt")
    except Exception as e:
        print(f"Ocurrio un error con el archivo: {e}")

    return prompt_file


@st.cache_resource(show_spinner=False)
def load_data():
    with st.spinner(text="Cargando e indexando documentos..."):
        reader = SimpleDirectoryReader(input_dir="./data", recursive=True)
        docs = reader.load_data()
        service_context = ServiceContext.from_defaults(
            llm=OpenAI(
                model="gpt-3.5-turbo",
                temperature=0.2,
                system_prompt=read_prompt()
            ))
        vector_index = VectorStoreIndex.from_documents(docs, service_context=service_context)
        return vector_index


index = load_data()

if "chat_engine" not in st.session_state.keys():  # Initialize the chat engine
    st.session_state.chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)

if prompt := st.chat_input("Tu pregunta"):  # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages:  # Display the prior chat messages
    with st.chat_message(message["role"]):
        st.write(message["content"])

# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            response = st.session_state.chat_engine.chat(prompt)
            st.write(response.response)
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message)  # Add response to message history
