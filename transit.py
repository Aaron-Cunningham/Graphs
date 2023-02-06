city_nodes = ['United Kingdom', 'Germany', 'France', 'USA', 'China']
city_edges = [('United Kingdom', 'United Kingdom'), ('United Kingdom', 'France'),
              ('France', 'Germany'), ('France', 'USA'), ('USA', 'China'), ('China', 'China')]

graph = {}
for node in city_nodes:
    graph[node] = []

for start_node, end_node in city_edges:
    graph[start_node].append(end_node)

for node in city_nodes:
    adjacent_nodes = graph[node]
    for connected_node in adjacent_nodes:
        for additional_node in graph[connected_node]:
            if additional_node not in adjacent_nodes:
                adjacent_nodes.append(additional_node)

print(graph)
