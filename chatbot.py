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

def getShortestPath(self):
    
        from network import G
        from database import location_names

        #Split the string into key words from the comma
        keywords = self.split(", ")

        selected_nodes = []

        #If there are any matching location words, fidn the index of them in the location_names database which is the same as the node key for the network
        for word in keywords:
            if word in location_names:
                node_id = location_names.index(word)
                selected_nodes.append(node_id)
            else:
                print("No matching locations")
        
        start = selected_nodes[0]
        target = selected_nodes[-1]
        
        # Find the shortest path w/ Dijkstra's magic
        path = nx.shortest_path(G, source=start, target=target)

        # Get the shortest path generated and use its location names so the AI can read it easily
        readable_path = [location_names[i] for i in path]
        path_directions = ', '.join(readable_path).replace(', ', ' -> ')

        print(path_directions)
        return f"The path is: {path_directions}"

shortestPathTool = Tool(
    name="Get Shortest Path",
    func=getShortestPath,
    description = "use this tool when you need to find the shortest path. Input in the following format: 'Location Start, Location Target' based on the key words"
)

def getCurrentLocation(input=""):
    from get_signal import strongest_node_address
    from database import router_addresses, location_names
    current_loc_key = router_addresses.index(strongest_node_address)
    current_loc_name = location_names[current_loc_key]
    return f"My Current Location is: {current_loc_name}"

currentLocationTool = Tool(
    name="Get Current Location",
    func=getCurrentLocation,
    description = "use this tool when you need to find your current location. input should be 'current_loc_name'"
)

def getDirections(self):
    from database import location_names, router_positions

    #Get the current location coordinates
    node_id = location_names.index(self)
    current_node_posX = router_positions[node_id][0]
    current_node_posY = router_positions[node_id][1]

    #Get the next location coordinates
    next_node_id = node_id + 1
    next_node_posX = router_positions[next_node_id][0]
    next_node_posY = router_positions[next_node_id][1]

    #calculate the direction vector
    x_dir = current_node_posX - next_node_posX
    y_dir = current_node_posY - next_node_posY
    
    if x_dir > 0 and y_dir > 0:
        return "Go North West"
    elif x_dir > 0 and y_dir < 0:
        return "Go South West"
    elif x_dir < 0 and y_dir > 0:
        return "Go North East"
    elif x_dir < 0 and y_dir < 0:
        return "Go South East"
    elif x_dir == 0 and y_dir > 0:
        return "Go North"
    elif x_dir == 0 and y_dir < 0:
        return "Go South"
    elif x_dir > 0 and y_dir == 0:
        return "Go West"
    elif x_dir < 0 and y_dir == 0:
        return "Go East"
    else: 
        return "You are traversing the 4th dimension and we cannot help you"
    
directionsTool = Tool(
    name="Get Directions",
    func=getDirections,
    description = "use this tool when you need to find the directions to the next location. input should be based on the User and remove any spaces or punctuation"
)

# initialize LLM (ChatGPT 3.5)
llm = ChatOpenAI(openai_api_key="apikey",
                 temperature=0)

# Tool List for the Agent
tools = [
    shortestPathTool, 
    currentLocationTool,
    directionsTool
]

# Initializing the Agent
agent = initialize_agent(tools, 
                         llm, 
                         agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, 
                         max_iterations=5, 
                         verbose=True,
                         handle_parsing_errors=True,
                        )

#Initializing the Streamlit Interface
st.title("Wilkinson Building Assistant")
question = st.text_input("Provide your question here")
if question:
    st.write(agent.run(question))  