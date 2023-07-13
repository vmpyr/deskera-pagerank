import networkx as nx

with open('testgraph.edgelist') as f:
    G = nx.read_weighted_edgelist(f)
    nx.write_graphml(G, 'testgraph.graphml')