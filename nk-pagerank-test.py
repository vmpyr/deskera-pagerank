import networkit as nk


g = nk.readGraph("./facebook.graphml", nk.Format.GraphML)

print(g.numberOfNodes(), g.numberOfEdges())

# couldn't find a way of plotting

pagerank_data = nk.centrality.PageRank(g, tol=1e-06).run().scores()

pagerank_values = {}
for i, val in enumerate(pagerank_data):
    pagerank_values[i+1] = val

pageranks = sorted(pagerank_values.items(), key=lambda v:(v[1],v[0]), reverse=True)

print("\nThe nodes ranked by page rank are\n")
for vertex, pgval in pageranks:
    print(vertex, end=" ")
print("\n")