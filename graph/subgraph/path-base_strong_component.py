from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v, visited, stack):
        visited[v] = True

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, stack)

        stack.append(v)

    def transpose(self):
        transposed_graph = Graph(self.V)

        for v in self.graph:
            for neighbor in self.graph[v]:
                transposed_graph.add_edge(neighbor, v)

        return transposed_graph

    def dfs_util(self, v, visited):
        visited[v] = True
        print(v, end=" ")

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited)

    def find_scc(self):
        stack = []
        visited = [False] * self.V

        for v in range(self.V):
            if not visited[v]:
                self.dfs(v, visited, stack)

        transposed_graph = self.transpose()

        visited = [False] * self.V

        while stack:
            v = stack.pop()
            if not visited[v]:
                transposed_graph.dfs_util(v, visited)
                print()


# Example usage
g = Graph(5)
g.add_edge(1, 0)
g.add_edge(0, 2)
g.add_edge(2, 1)
g.add_edge(0, 3)
g.add_edge(3, 4)

print("Strongly Connected Components:")
g.find_scc()
