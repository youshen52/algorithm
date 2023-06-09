import numpy as np
import networkx as nx


def pagerank(graph, damping_factor=0.85, max_iterations=100, tolerance=1e-6):
    num_nodes = len(graph)
    adjacency_matrix = nx.adjacency_matrix(graph).toarray()
    out_degree = np.sum(adjacency_matrix, axis=1)
    transition_matrix = adjacency_matrix / out_degree[:, np.newaxis]
    teleportation_matrix = np.full((num_nodes, num_nodes), 1 / num_nodes)

    rank = np.full(num_nodes, 1 / num_nodes)
    for _ in range(max_iterations):
        new_rank = ((1 - damping_factor) / num_nodes) + (
            damping_factor * transition_matrix.T @ rank
        )
        if np.linalg.norm(new_rank - rank) < tolerance:
            break
        rank = new_rank

    return rank
