import heapq
import dijkstra, bellman_ford


def johnson(graph):
    # Add a new node connected to all other nodes with weight 0
    graph_with_extra_node = graph.copy()
    extra_node = "extra_node"
    for node in graph_with_extra_node:
        graph_with_extra_node[node][extra_node] = 0

    # Run Bellman-Ford algorithm to compute h values
    h = bellman_ford(graph_with_extra_node, extra_node)
    del h[extra_node]

    # Recalculate edge weights using h values
    graph_with_reweighted_edges = {}
    for node in graph:
        graph_with_reweighted_edges[node] = [
            (neighbor, weight + h[node] - h[neighbor])
            for neighbor, weight in graph[node]
        ]

    # Run Dijkstra's algorithm for each node to get shortest paths
    shortest_paths = {}
    for node in graph:
        shortest_paths[node] = dijkstra(graph_with_reweighted_edges, node)

    # Adjust distances to original weights using h values
    for node in shortest_paths:
        for dest in shortest_paths[node]:
            shortest_paths[node][dest] += h[dest] - h[node]

    return shortest_paths
