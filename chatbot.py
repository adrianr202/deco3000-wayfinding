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

tools = [
    Tool(
        name="Differentiate Events",
        #func=wiki.search,
        description="Search for an article on Wikipedia",
    ),
    Tool(
        name="Differentiate Room Numbers",
        #func=wiki.lookup,
        description="Look up a term within the last article retrieved from Wikipedia. You cannot use this tool until you have used the Search tool to find an Article.",
    ),
    Tool(
        name="Get Current Location",
        #func = writer_chain.run,
        description="An LLM prompted for creative writing about a provided topic"
    ),
    Tool(
        name="Get Target Location",
        #func = writer_chain.run,
        description="An LLM prompted for creative writing about a provided topic"
    )
]

direction_template = PromptTemplate(
    input_variables=["direction"],
    template="""Provide direction to the locations and provide a map of the building. Provide the schedule also.
    
    {direction}
    """
)

agent_kwargs = {
    "prefix": "Answer the following questions as best you can, making sure always to answer in the form of Rudyard Kipling's poem: Buddha at Kamakura (1892)",
    "format_instructions": """
    Use the following format:

    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be one of [Search, Lookup]
    Action Input: the input to the action
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    Thought: I now know the final answer
    Final Answer: Poem about the topic in the style of Rudyard Kipling's Buddha at Kamakura (1892)
    """
}

direction_chain = LLMChain(llm=llm, prompt=direction_template, verbose=True)
overall_chain= SimpleSequentialChain(chains=[determine_user_purpose_chain, direction_chain], verbose=True)

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, max_iterations=5, agent_kwargs=agent_kwargs)

st.title("Wilkinson Building Assistant")
question = st.text_input("What brings you here today?")

if question:
    st.write(agent.run(question))

