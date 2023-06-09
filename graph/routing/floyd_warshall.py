def floyd_warshall(graph):
    # Initialization
    distances = graph

    # Main algorithm
    num_nodes = len(graph)
    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                distances[i][j] = min(
                    distances[i][j], distances[i][k] + distances[k][j]
                )

    return distances
