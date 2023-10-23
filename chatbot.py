from curses import init_pair
from tabnanny import verbose
from unicodedata import name
from apikey import apikey
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain
from langchain.llms import OpenAI
from langchain.chains import SimpleSequentialChain

# Week 8 imports
from langchain.agents import Tool, AgentType, initialize_agent
from langchain.agents.react.base import DocstoreExplorer
from langchain.docstore.wikipedia import Wikipedia
import langchain 

import time

langchain.verbose = True

import streamlit as st

llm = ChatOpenAI(openai_api_key=apikey)

def slowcall(function,delay=2):
    time.sleep(delay)
    return function
    

# Features include
# Room Number
# Intention of staying at Wilkinson
    # Study
    # Lecture
    # Class / Studio / Workshop
    # Guest Speaker

# Prompts the user to specify the purpose of their stay at a Wilkinson and returns their response.
determine_user_purpose = PromptTemplate(
    input_variables=["purpose"],
    
    # Please describe the purpose of your stay at Wilkinson. 
    # You may include details such as the nature of your visit, the duration, and any specific requirements.
    template="""Return a schedule with {purpose} in a hourly format table. Show the time, task and location in this table"""     
)

determine_user_purpose_chain = LLMChain(llm=llm, prompt=determine_user_purpose, verbose=True)

direction_template = PromptTemplate(
    input_variables=["direction"],
    template="""Provide direction to the locations and provide a map of the building. Provide the schedule also.
    
    {direction}
    """
)

direction_chain = LLMChain(llm=llm, prompt=direction_template, verbose=True)

overall_chain= SimpleSequentialChain(chains=[determine_user_purpose_chain, direction_chain], verbose=True)

st.title("Wilkinson Building Assistant")
question = st.text_input("What brings you here today?")

if question:
    st.write(overall_chain.run(question))

