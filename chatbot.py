from langchain.tools import BaseTool
from langchain.agents import Tool, AgentType, initialize_agent
import langchain 

langchain.verbose = True

import streamlit as st

from langchain.chat_models import ChatOpenAI

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Import the strongest_node function from get_signal.py, function cus circular import error
from database import router_addresses, location_names, connections

#Create a graph
G = nx.Graph()

# Node Constructor based on a Key with attributes: bssid, name
for i in range(len(router_addresses)):
    G.add_node(i, 
               bssid=router_addresses[i], 
               name=location_names[i]
               )
    
# Add edges (connections/hallways) between nodes
G.add_edges_from(connections)

def getShortestPath(input=""):
        
        #What is the shortest path between Entrance Inside and Homebase Storage

        #Split the string into key words from the comma
        keywords = input.split(", ")

        #Compare the words from the words in the database
        from database import location_names

        selected_nodes = []

        #If there are any matching location words, fidn the index of them in the location_names database which is the same as the node key for the network
        for word in keywords:
            if word in location_names:
                node_id = location_names.index(word)
                selected_nodes.append(node_id)
            else:
                print("No matching locations")
        
        #for some reason network.py cannot import this, so Ill use static values for now in network.py
        start = selected_nodes[0]
        target = selected_nodes[-1]
        
        # Find the shortest path w/ Dijkstra's magic
        path = nx.shortest_path(G, source=start, target=target)

        # Get the shortest path generated and use its location names so the AI can read it easily
        readable_path = [location_names[i] for i in path]
        path_directions = ', '.join(readable_path).replace(', ', ' -> ')

        print(path_directions)
        return path_directions


# initialize LLM (ChatGPT 3.5)
llm = ChatOpenAI(openai_api_key="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",
                 temperature=0)

# Tool List for the Agent
tools = [
    Tool(
        name="Get Shortest Path",
        func=getShortestPath,
        description = "use this tool when you need to find the shortest path. Input in the following format: 'Entrance Outside, Homebase Storage' based on the key words"
    )
]

# Agent Kwargs, layout of how the agent will ask questions
agent_kwargs = {
    "prefix": "Answer the following questions as best you can, making sure always to answer using the format instructions",
    "format_instructions": """
    Use the following format:

    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, what should I check to get the answer to the question? To be able
    Action Input: the input to the action
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    Thought: I now know the final answer

    Final Answer: What is the Next Step?
    """
}

# Initializing the Agent
agent = initialize_agent(tools, 
                         llm, 
                         agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, 
                         max_iterations=3, 
                         agent_kwargs=agent_kwargs,
                         verbose=True,
                         handle_parsing_errors=True,
                        )

#Initializing the Streamlit Interface
st.title("Wilkinson Building Assistant")
question = st.text_input("Provide your question here")
if question:
    st.write(agent.run(question))  