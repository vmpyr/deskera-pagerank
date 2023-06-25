import graph_tool.all as gt


g = gt.collection.ns["ego_social/facebook_0"]

gt.graph_draw(g, g.vp._pos, output_size=(1000, 1000))

pr = gt.pagerank(g)

pagerank_values = {}
for vertex in g.vertices():
    pagerank_values[vertex] = pr[vertex]

pageranks = sorted(pagerank_values.items(), key=lambda v:(v[1],v[0]), reverse=True)

print("\nThe nodes ranked by page rank are\n")
for vertex, pgval in pageranks:
    print(vertex, end=" ")
print("\n")
