def is_subgraph(graph, subgraph):
    for node in subgraph:
        if node not in graph:
            return False
        for neighbor in subgraph[node]:
            if neighbor not in graph[node]:
                return False
    return True


# Example usage
graph = {
    "A": ["B", "C", "D"],
    "B": ["C"],
    "C": ["D", "E"],
    "D": [],
    "E": ["F"],
    "F": [],
}

subgraph = {"A": ["B", "C"], "C": ["D"]}

if is_subgraph(graph, subgraph):
    print("The subgraph is a subgraph of the graph.")
else:
    print("The subgraph is not a subgraph of the graph.")
