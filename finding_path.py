# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 21:59:15 2018

@author: Lenovo
"""

"""
Algorithm

start at node1
node1 neighbor
check for destination ., if not continue..
continue till we reach the destination node.

Breath first search algorithm"""
import networkx as nx
import datetime
#reading the network file
G=nx.read_gpickle("ego-twitter.p")

len(G.edges())

len(G.nodes())

G.neighbors(1)

G.neighbors(10)

#finding distance from node 1 to 19.
# node 1 ---> node 10 ---> node 19 ., stop algorithm

