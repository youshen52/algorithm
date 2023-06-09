class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * self.V for _ in range(self.V)]

    def add_edge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1

    def bron_kerbosch(self, r, p, x, cliques):
        if not any((p, x)):
            cliques.append(r)
            return

        for v in list(p):
            nv = set()
            r.append(v)
            for neighbor in p:
                if self.graph[v][neighbor]:
                    nv.add(neighbor)
            np = set()
            for neighbor in p:
                if self.graph[v][neighbor] == 0 and not self.has_common_neighbors(
                    v, neighbor
                ):
                    np.add(neighbor)
            nx = set()
            for neighbor in x:
                if self.graph[v][neighbor] == 0 and not self.has_common_neighbors(
                    v, neighbor
                ):
                    nx.add(neighbor)
            self.bron_kerbosch(r, np, nx, cliques)
            r.remove(v)
            p.remove(v)
            x.add(v)

    def has_common_neighbors(self, u, v):
        for i in range(self.V):
            if self.graph[u][i] and self.graph[v][i]:
                return True
        return False

    def find_cliques(self):
        r = []
        p = set(range(self.V))
        x = set()
        cliques = []
        self.bron_kerbosch(r, p, x, cliques)
        return cliques


# Example usage
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 4)

cliques = g.find_cliques()
print("Maximal Cliques:")
for clique in cliques:
    print(clique)
