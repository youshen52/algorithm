import random


def karger_algorithm(graph):
    num_vertices = len(graph)
    min_cut = float("inf")

    # Contract edges until only 2 vertices are left
    for _ in range(num_vertices - 2):
        # Create a copy of the graph to modify
        contracted_graph = graph.copy()

        # Contract a randomly selected edge until only 2 vertices are left
        while len(contracted_graph) > 2:
            u = random.choice(list(contracted_graph.keys()))
            v = random.choice(list(contracted_graph[u]))

            # Merge vertices u and v
            contracted_graph[u].extend(contracted_graph[v])
            for vertex in contracted_graph[v]:
                contracted_graph[vertex].remove(v)
                contracted_graph[vertex].append(u)
            del contracted_graph[v]

            # Remove self-loops
            contracted_graph[u] = [
                vertex for vertex in contracted_graph[u] if vertex != u
            ]

        # Update the minimum cut if necessary
        min_cut = min(min_cut, len(contracted_graph[list(contracted_graph.keys())[0]]))

    return min_cut
