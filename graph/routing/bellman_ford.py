def bellman_ford(graph, start):
    # Initialization
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    # Relax edges repeatedly
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node]:
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    # Check for negative cycles
    for node in graph:
        for neighbor, weight in graph[node]:
            if distances[node] + weight < distances[neighbor]:
                raise ValueError("Negative cycle detected")

    return distances
