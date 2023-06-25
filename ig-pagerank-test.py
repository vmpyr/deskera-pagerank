import igraph as ig
import matplotlib.pyplot as plt


g = ig.Graph.Erdos_Renyi(333, m=2519, directed=False)

fig, ax=plt.subplots()
ig.plot(g, target=ax)
plt.show()

pagerank_data = ig.Graph.pagerank(g)

pagerank_values = {}
for i, val in enumerate(pagerank_data):
    pagerank_values[i+1] = val

pageranks = sorted(pagerank_values.items(), key=lambda v:(v[1],v[0]), reverse=True)

print("\nThe nodes ranked by page rank are\n")
for vertex, pgval in pageranks:
    print(vertex, end=" ")
print("\n")