import networkx as nx
import matplotlib.pyplot as plt

# created a directed graph
graph=nx.fast_gnp_random_graph(25, 0.6, seed=123, directed=False)

# draw a graph
nx.draw(graph, with_labels=True, font_color='white', font_size=10, node_color='teal', edge_color='purple')

# plot a graph
plt.show()

# number of nodes for graph
count = graph.number_of_nodes()
print(f"Number of nodes in the graph are {count}")

# Page rank by networkx library
pagerank_values = nx.pagerank(graph)

# sorting the pagerank_values dictionary based on items
pageranks = sorted(pagerank_values.items(),key=lambda v:(v[1],v[0]),reverse=True)

print("\nThe nodes ranked by page rank are\n")
for i in pageranks:
    print(i[0], end=" ")
print("\n")
