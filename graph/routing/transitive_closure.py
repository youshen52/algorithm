def transitive_closure(graph):
    # Initialization
    closure = {node: set() for node in graph}

    # Compute transitive closure using Warshall's algorithm
    for k in graph:
        for i in graph:
            for j in graph:
                if i != j and i != k and j != k and (i, k) in graph and (k, j) in graph:
                    closure[i].add(j)

    return closure
