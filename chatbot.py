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

# Import Wilkinson Custom Database and tools
from wilkinson_database.database import purpose_database, room_database  # Import purpose and landmarks

def search_purpose_database(input_text):
    input_text = input_text.lower()  # Convert user input to lowercase for case-insensitive search
    for purpose, data in purpose_database.items():
        descriptions = data["descriptions"]
        keywords = data["keywords"]
        for keyword in keywords:
            if keyword in input_text:
                return f"You seem to be here for {purpose} ({', '.join(descriptions)})."
    return "I'm not sure about your purpose here."

# Tool for room details
def room_finder(room_number):
    room_info = room_database.get(room_number)
    if room_info:
        st.write(f"**Room {room_number}**")
        st.write(f"**Name:** {room_info['name']}")
        st.write(f"**Capacity:** {room_info['capacity']} people")
        st.write(f"**Description:** {room_info['description']}")
        st.button("Directions")
    else:
        return f"Room {room_number} not found in the building."

def display_location_info(location_name):
    st.write(f"Here are the directions to {location_name}")

llm = ChatOpenAI(openai_api_key=apikey)

def slowcall(function,delay=2):
    time.sleep(delay)
    return function

# Function to display information and directions for a location

# Features include
# Room Number
# Intention of staying at Wilkinson
    # Study
    # Lecture
    # Class / Studio / Workshop
    # Guest Speaker

# Prompts the user to specify the purpose of their stay at a Wilkinson and returns their response.

tools = [
    Tool(
        name="Determine Purpose",
        func=search_purpose_database,
        description="Determine the user's purpose in Wilkinson Building based on their input."
    ),
    Tool(
        name="Differentiate Room Numbers",
        func=room_finder,
        description="Find information about a room by entering its room number.",
    ),
    # Tool(
    #     name="Get Current Location",
    #     #func = writer_chain.run,
    #     description="Capture current location for localization"
    # ),
    # Tool(
    #     name="Get Target Location",
    #     #func = writer_chain.run,
    #     description="Capture target room location"
    # )
]

agent_kwargs = {
    "prefix": "Answer the following questions as best you can, making sure always to answer using the format instructions",
    "format_instructions": """
    Use the following format:

    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be one of these tools [Determine Purpose], [Differentiate Room Number]
    Action Input: the input to the action
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    Thought: I now know the final answer

    Final Answer: You seem to have [Purpose] at [Room], would you like directions to it?
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
         