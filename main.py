from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from pathlib import Path
from langchain.prompts import ChatPromptTemplate
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from db import *
from memory import *

load_dotenv()

CONDENSE_PROMPT = (Path("assets/condense_prompt.txt").read_text()).strip()
QA_PROMPT = (Path("assets/prompt.txt").read_text()).strip()
prompt = ChatPromptTemplate.from_template(QA_PROMPT)
con_prompt = PromptTemplate.from_template(CONDENSE_PROMPT)

vectorstore = milvusDB()

memory = CSBM()

model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.2)

qa = ConversationalRetrievalChain.from_llm(
    model,
    vectorstore.as_retriever(),
    memory=memory,
    combine_docs_chain_kwargs={"prompt": prompt},
    condense_question_prompt=con_prompt
)
