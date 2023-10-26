#from curses import init_pair
#from tabnanny import verbose
from unicodedata import name
from apikey import apikey
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate, LLMChain
from langchain.llms import OpenAI
from langchain.chains import SimpleSequentialChain

# Week 8 imports
from langchain.agents import Tool, AgentType, initialize_agent
from langchain.tools import BaseTool
import langchain 

langchain.verbose = True

import streamlit as st

#Import shortest path algorithm
from network import path_edges

# Import Wilkinson Custom Database and tools
from wilkinson_database.database import purpose_database, room_database  # Import purpose and landmarks

class DeterminePurpose(BaseTool):
    name = "Determine Purpose"
    description = "Determine the user's purpose in Wilkinson Building based on their input."

    def _run(self, input_text):
        # lowercase the input text
        input_text = input_text.lower()

        # iterate through the purpose database
        for purpose, data in purpose_database.items():
            keywords = data["keywords"]
            for keyword in keywords:
                if keyword in input_text:
                    return f"You seem to be here for {purpose}."
        return "I'm not sure about your purpose here."
    
    def _arun(self):
        return "ASYNC ERROR."

class FindRoom(BaseTool):
    name = "Find Room"
    description = "Find information about a room by entering its room number."

    def _run(self, input_text):
        # lowercase the input text
        input_text = input_text.lower()

        # iterate through the purpose database
        for room_number, data in room_database.items():
            if room_number in input_text:
                name = data["name"]
                description = data["description"]
                return f"**Room {room_number}**\n**Name:** {name}\n**Description:** {description}"
        return "I'm not sure about the room you're looking for."

    def _arun(self):
        return "ASYNC ERROR."

llm = ChatOpenAI(openai_api_key='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')

tools = [
    DeterminePurpose(),
    FindRoom(),
]

agent_kwargs = {
    "prefix": "Answer the following questions as best you can, making sure always to answer using the format instructions",
    "format_instructions": """
    Use the following format:

    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be the list of tools available
    Action Input: the input to the action
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    Thought: I now know the final answer

    Final Answer: [Room] is the best for [Purpose], would you like directions to it?
    """
}

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, max_iterations=5, agent_kwargs=agent_kwargs)
st.title("Wilkinson Building Assistant")

# seperate feature points of chatbot
# Tab 1 - Directory
# Tab 2 - Advanced Help
tab1, tab2 = st.tabs(["Directory", "Further Help"])

with tab1:
    st.header("Directory")
    st.write("Click on a location for directions")

    # Define the locations as a list of text values
    locations = [
        "Masters Homebase",
        "DECO3000 - Tutorial Session",
        "DECO3000 - Lecture Session",
        "Tin Sheds Gallery",
    ]

    # Horizontal layout for the buttons
    num_columns = len(locations)
    columns = st.columns(num_columns)

    for i, location_name in enumerate(locations):
        if columns[i].button(location_name):
            # outputs the direction to clicked location button
            display_location_info(location_name)

with tab2:
    st.header("Still need help?")
    question = st.text_input("Provide your question here")

    if question:
        st.write(agent.run(question)) 

    room_number = st.text_input("Enter a room number to find information:").lower()
    if room_number:
        room_info = room_finder(room_number)
         