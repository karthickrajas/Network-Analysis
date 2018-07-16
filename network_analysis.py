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

