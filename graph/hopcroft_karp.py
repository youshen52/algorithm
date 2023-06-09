class BipartiteMatching:
    def __init__(self, graph):
        self.graph = graph
        self.M = len(graph)
        self.N = len(graph[0])
        self.pairU = [-1] * self.M
        self.pairV = [-1] * self.N
        self.dist = [0] * self.M

    def bfs(self):
        queue = []
        for u in range(self.M):
            if self.pairU[u] == -1:
                self.dist[u] = 0
                queue.append(u)
            else:
                self.dist[u] = float("inf")

        self.dist[-1] = float("inf")

        while queue:
            u = queue.pop(0)
            if self.dist[u] < self.dist[-1]:
                for v in range(self.N):
                    if self.graph[u][v] and self.dist[self.pairV[v]] == float("inf"):
                        self.dist[self.pairV[v]] = self.dist[u] + 1
                        queue.append(self.pairV[v])

    def dfs(self, u):
        if u == -1:
            return True
        for v in range(self.N):
            if (
                self.graph[u][v]
                and self.dist[self.pairV[v]] == self.dist[u] + 1
                and self.dfs(self.pairV[v])
            ):
                self.pairU[u] = v
                self.pairV[v] = u
                return True
        self.dist[u] = float("inf")
        return False

    def hopcroft_karp(self):
        matching = 0
        while True:
            self.bfs()
            flow = sum(self.dfs(u) for u in range(self.M) if self.pairU[u] == -1)
            if flow == 0:
                break
            matching += flow
        return matching


# Example usage:
graph = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1],
]
bm = BipartiteMatching(graph)
print("Maximum Cardinality Matching:", bm.hopcroft_karp())
