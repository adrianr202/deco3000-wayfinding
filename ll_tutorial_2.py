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
    time.sleep(delay),
    return function


# country_template = PromptTemplate(
#     input_variables=["topic"],
#     template="""Return a suitable country that associates with {topic}.
#     """
# )

# country_chain = LLMChain(llm=llm, prompt=country_template, verbose=True)

# intinerary_template = PromptTemplate(
#     input_variables=["place"],
#     template = """Return a place into an itinerary for {place}. """
# )

# itinerary_chain = LLMChain(llm=llm, prompt=intinerary_template, verbose=True)


wiki = DocstoreExplorer(Wikipedia())
tools = [
    Tool(
        name = "Search for Article",
        func = wiki.search,
        description = "Search for an article on Wikipedia."
    ),
    Tool(
        name = "Lookup within Article",
        func = wiki.lookup,
        description = "Look up a term within the last article retrieved from Wikipedia. You cannot use this tool until you have retrieved an article from the search tool."
    ),
]

agent_kwargs = {
    "prefix": "Answer the following questions as best you can, making sure to always to answer in the form of a checklist. You have access to the following tools",
    "format_instructions": """Use the following format:

    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be one of {tool_names}
    Action Input: the input to the action
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    Thought: I now know the final answer

    Final Answer: 
    
    """,
}

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, max_iterations=5) # agent_kwargs=agent_kwargs)
print(agent.agent.llm_chain.prompt.template)

st.title("Holiday simulator")
question = st.text_input("What would you like to do for a holiday?")

if question:
    st.write(agent.run(question))

