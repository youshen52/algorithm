def nearest_neighbor(graph, start):
    path = [start]
    current_node = start

    while len(path) < len(graph):
        next_node = None
        min_dist = float("inf")

        for neighbor, weight in graph[current_node]:
            if neighbor not in path and weight < min_dist:
                next_node = neighbor
                min_dist = weight

        path.append(next_node)
        current_node = next_node

    return path
