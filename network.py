import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Import the strongest_node function from get_signal.py, function cus circular import error
from database import router_addresses, location_names, connections, router_positions

# If you want your Local network to be used, Go to database.py and change 'ADD LOCAL ROUTER' to your router's MAC address

# Create a graph
G = nx.Graph()

# Node Constructor based on a Key with attributes: bssid, name
for i in range(len(router_addresses)):
    G.add_node(i, 
               bssid=router_addresses[i], 
               name=location_names[i]
               )
    
# Add edges (connections/hallways) between nodes
G.add_edges_from(connections)

#In reality, these numbers would be represented with the keys of the nodes, changing with each time to the closest one, 
#but for proof of concept, showing static values is easier.

#supposed to be imported from chatbot.py but not working for some reason so using static values
start = 1
target = 10

# Find the shortest path w/ Dijkstra's magic
path = nx.shortest_path(G, source=start, target=target)

# Get the shortest path generated and use its location names so the AI can read it easily
readable_path = [location_names[i] for i in path]
string_path = ', '.join(readable_path).replace(', ', ' -> ')
print(string_path)

#Code Below is to visually display the Wilkinson map showing how it is. 
#Not necessary for the program but allows visualization of how the nodes can map an indoor space

#Create a figure and axis
plt.figure(figsize=(14.2, 13.0))
ax = plt.gca()
ax.set_xlim(0, 142)  # Set minimum and maximum X-axis values
ax.set_ylim(0, 130)

#Draw the Nodes
nx.draw(G, router_positions, 
        with_labels=True, 
        node_size=300, 
        node_color='grey', 
        font_size=8, 
        font_color='blue',
        labels={node: G.nodes[node]['name'] for node in G.nodes} # Label each node with its name, I'll admit I don't know how this line works, but Github Copilot is awesome
        )

# Highlight the shortest path
path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
nx.draw_networkx_edges(G, router_positions, edgelist=connections, edge_color='w', width=2)
nx.draw_networkx_edges(G, router_positions, edgelist=path_edges, edge_color='r', width=2)

# Get the shortest path generated and use its location names os the AI can read it easily
sorted_path = list(set(item for pair in path_edges for item in pair))
readable_path = [location_names[i] for i in sorted_path]

# Show the plot with Wilkinson Building map overlay + title
image = mpimg.imread('wilko_level2.png')
plt.title("Wilkinson Building (G04), Level 2")
ax.imshow(np.array(image), extent=[0, 142, 0, 130])

plt.show()