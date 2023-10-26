import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Create a graph
G = nx.Graph()

# Node Constructor based on each Router
class RouterNode:
    def __init__(self, key, bssid):
        self.key = key
        self.bssid = bssid
    pass

router_addresses = [
    'Start',                        # 0
    '48:91:d5:ef:2c:b8',            # 1 
    '48:91:d5:ee:fd:80',            # 2 
    '48:91:d5:ee:d7:38',            # 3 
    '48:91:d5:ee:ba:b0',            # 4 
    '48:91:d5:ee:fa:18',            # 5 
    '48:91:d5:ee:ae:b0',            # 6 
    '48:91:d5:ef:00:10',            # 7 
    '48:91:d5:ee:b7:2c',            # 8
    '48:91:d5:ef:2d:50',            # 9 
    '48:91:d5:ef:25:a8 (Target)'    # 10
    ]

# Add node for each router using the RouterNode constructor
for i in range(len(router_addresses)):
    node = RouterNode(i, router_addresses[i])
    G.add_node(node.key)

# Create a figure and axis
plt.figure(figsize=(14.2, 13.0))
ax = plt.gca()
ax.set_xlim(0, 142)  # Set minimum and maximum X-axis values
ax.set_ylim(0, 130)

# Add edges (connections/hallways)
connections = [
    (0, 1), 
    (1, 2), 
    (2, 3), 
    (2, 4),
    (3, 4),
    (3, 5),
    (4, 5),
    (5, 6),
    (6, 7),
    (6, 9),
    (7, 8),
    (8, 9),
    (9, 10),
    ]

G.add_edges_from(connections)

router_positions = {
    0: (70, 96),
    1: (73, 81),
    2: (54, 77),
    3: (38, 66),
    4: (29, 79),
    5: (23, 49),
    6: (24, 31),
    7: (40, 24),
    8: (42, 46),
    9: (53, 36),
    10: (57, 47),
}

# Draw the Nodes
nx.draw(G, router_positions, 
        with_labels=True, 
        node_size=300, 
        node_color='green', 
        font_size=10, 
        font_color='white')

# Set the start and target nodes
start = 0
target = 10

# Find the shortest path
path = nx.shortest_path(G, source=start, target=target)

# Highlight the shortest path
path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
nx.draw_networkx_edges(G, router_positions, edgelist=connections, edge_color='white', width=2)
nx.draw_networkx_edges(G, router_positions, edgelist=path_edges, edge_color='r', width=2)

# Show the plot with Wilkinson Building map overlay + title
image = mpimg.imread('wilko_level2.png')
plt.title("Wilkinson Building (G04), Level 2")
ax.imshow(np.array(image), extent=[0, 142, 0, 130])
plt.show()