from graph_tool.centrality import pagerank
from graph_tool import load_graph
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("path")
args = parser.parse_args()
g = load_graph(args.path)

# gt.graph_draw(g, g.vp._pos, output_size=(1000, 1000))
pr = pagerank(g, weight=g.edge_properties['weight'])

pagerank_values = {}
for vertex in g.get_vertices():
    pagerank_values[vertex+1] = pr[vertex]

pageranks = sorted(pagerank_values.items(), key=lambda v:(v[1],v[0]), reverse=True)

print("\nThe nodes ranked by page rank are\n")
for vertex, pgval in pageranks:
    print(vertex, end=" ")
print("\n")
