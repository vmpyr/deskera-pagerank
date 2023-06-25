import networkx as nx
import matplotlib.pyplot as plt


g = nx.fast_gnp_random_graph(333, 0.6, seed=123, directed=False)

nx.draw(g, with_labels=True, font_color='white', font_size=10, node_color='teal', edge_color='purple')
plt.show()


pagerank_values = nx.pagerank(g)

pageranks = sorted(pagerank_values.items(), key=lambda v:(v[1],v[0]), reverse=True)

print("\nThe nodes ranked by page rank are\n")
for i in pageranks:
    print(i[0], end=" ")
print("\n")
