class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * self.V for _ in range(self.V)]

    def add_edge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1

    def max_clique_dyn(self, subset, size, depth, counter):
        if depth == self.V:
            return

        for i in range(depth, self.V):
            if size + counter[i] <= self.V:
                return

            if self.is_clique(subset + [i], size):
                if size + 1 > counter[0]:
                    counter[0] = size + 1
                self.max_clique_dyn(subset + [i], size + 1, i + 1, counter)

    def is_clique(self, subset, size):
        for i in range(size):
            for j in range(i + 1, size):
                if self.graph[subset[i]][subset[j]] == 0:
                    return False
        return True

    def find_maximum_clique(self):
        counter = [0]
        self.max_clique_dyn([], 0, 0, counter)
        return counter[0]


# Example usage
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 4)

maximum_clique_size = g.find_maximum_clique()
print("Maximum Clique Size:", maximum_clique_size)
