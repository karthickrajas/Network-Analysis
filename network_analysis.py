# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 21:59:16 2018

@author: Lenovo
"""

import networkx as nx
import datetime
#reading the network file
G=nx.read_gpickle("ego-twitter.p")


#checking the structure of the nodes and edges
G.nodes()
G.edges()
G.nodes(data=True)

# Use a list comprehension to get the nodes of interest: noi
noi = [n for n, d in G.nodes(data = True) if d['occupation'] == 'scientist']

# Use a list comprehension to get the edges of interest: eoi
eoi = [(u, v) for u, v, d in G.edges(data=True) if d['date'] < datetime.date(2010, 1, 1)]

# Set the weight of the edge
G.edge[1][10]['weight'] = 2

# Iterate over all the edges (with metadata)
for u, v, d in G.edges(data=True):

    # Check if node 293 is involved
    if 293 in [u,v]:
    
        # Set the weight to 1.1
        G.edge[u][v]['weight'] = 1.1
        
## Visualising networks

""" matrix plot
arc plot
circos plot"""


import matplotlip.pyplot as plt

# Import nxviz
import nxviz as nv

# Create the MatrixPlot object: m
m = nv.MatrixPlot(G)

# Draw m to the screen
m.draw()

# Display the plot
plt.show()

# Convert T to a matrix format: A
A = nx.to_numpy_matrix(G)

# Convert A back to the NetworkX form as a directed graph: T_conv
T_conv = nx.from_numpy_matrix(A, create_using=nx.DiGraph())

# Check that the `category` metadata field is lost from each node
for n, d in T_conv.nodes(data=True):
    assert 'category' not in d.keys()
    
# Import necessary modules
import matplotlib.pyplot as plt
from nxviz import CircosPlot

# Create the CircosPlot object: c
c = CircosPlot(G)

# Draw c to the screen
c.draw()

# Display the plot
plt.show()


# Import necessary modules
import matplotlib.pyplot as plt
from nxviz import ArcPlot

# Create the un-customized ArcPlot object: a
a = ArcPlot(G)

# Draw a to the screen
a.draw()

# Display the plot
plt.show()

# Create the customized ArcPlot object: a2
a2 = ArcPlot(G, node_order='category', node_color='category')

# Draw a2 to the screen
a2.draw()

# Display the plot
plt.show()

# Finding the nodes with m number of neighbours


# Define nodes_with_m_nbrs()
def nodes_with_m_nbrs(G,m):
    """
    Returns all nodes in graph G that have m neighbors.
    """
    nodes = set()
    
    # Iterate over all nodes in G
    for n in G.nodes():
    
        # Check if the number of neighbors of n matches m
        if len(G.neighbors(n)) == m:
        
            # Add the node n to the set
            nodes.add(n)
            
    # Return the nodes with m neighbors
    return nodes

# Compute and print all nodes in T that have 6 neighbors
six_nbrs = nodes_with_m_nbrs(G,6)
print(six_nbrs)


# Compute the degree of every node: degrees
degrees = [len(G.neighbors(n)) for n in G.nodes()]

# Print the degrees
print(degrees)

# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Compute the degree centrality of the Twitter network: deg_cent
deg_cent = nx.degree_centrality(G)

# Plot a histogram of the degree centrality distribution of the graph.
plt.figure()
plt.hist(list(deg_cent.values()))
plt.show()

# Plot a histogram of the degree distribution of the graph
plt.figure()
plt.hist(degrees)
plt.show()

# Plot a scatter plot of the centrality distribution and the degree distribution
plt.figure()
plt.scatter(degrees,list(deg_cent.values()))
plt.show()

