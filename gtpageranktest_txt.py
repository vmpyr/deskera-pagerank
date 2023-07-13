from graph_tool.centrality import pagerank
from graph_tool import Graph
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("path")
args = parser.parse_args()

g = Graph(directed=False)
edge_list = []
with open(args.path, 'r') as f:
    data = f.read().splitlines()
    for line in data:
        if len(line)==0:
            continue
        if line[0]=='#':
            continue
        edge_list.append(tuple(map(float, line.split())))

g.add_edge_list(edge_list, eprops=[('weights', "double")])

# print(g.get_all_neighbors(0))
# gt.graph_draw(g, g.vp._pos, output_size=(1000, 1000))
pr = pagerank(g, weight=g.edge_properties['weights'])

pagerank_values = {}
for vertex in g.get_vertices():
    pagerank_values[vertex] = pr[vertex]

pageranks = sorted(pagerank_values.items(), key=lambda v:(v[1],v[0]), reverse=True)

print("\nThe nodes ranked by page rank are\n")
for vertex, pgval in pageranks:
    print(vertex, end=" ")
print("\n")