import networkx as nx


def girvan_newman(graph):
    def find_communities(graph):
        if len(graph.edges()) == 0:
            return [list(graph.nodes())]

        betweenness = nx.edge_betweenness_centrality(graph)
        max_betweenness = max(betweenness.values())
        edges_to_remove = [
            edge for edge, score in betweenness.items() if score == max_betweenness
        ]

        communities = []
        for edge in edges_to_remove:
            graph.remove_edge(*edge)
            components = nx.connected_components(graph)
            communities = [list(component) for component in components]

        return communities

    communities = []
    while True:
        components = nx.connected_components(graph)
        new_communities = [list(component) for component in components]
        if len(new_communities) == len(communities):
            break
        communities = new_communities
        graph.remove_edges_from(graph.edges())

    return communities
