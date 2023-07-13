import graph_tool.all as gt

g = gt.Graph()
eweight = g.new_ep("double")

edge_list = []
with open('testgraph.edgelist', 'r') as f:
    data = f.read().splitlines()
    print(data)
    for line in data:
        if line[0]=='#':
            continue
        edge_list.append(tuple(map(float, line.split())))

print(edge_list)
g.add_edge_list(edge_list, eprops=[eweight])