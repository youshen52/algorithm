from collections import defaultdict
from time import time as my_time


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.time = 0

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def tarjan_scc(self):
        visited = [-1] * self.V
        low_link = [-1] * self.V
        stack_member = [False] * self.V
        stack = []
        result = []

        def strong_connect(v):
            nonlocal stack, stack_member, visited, low_link, result

            visited[v] = self.time
            low_link[v] = self.time
            self.time += 1
            stack.append(v)
            stack_member[v] = True

            for neighbor in self.graph[v]:
                if visited[neighbor] == -1:
                    strong_connect(neighbor)
                    low_link[v] = min(low_link[v], low_link[neighbor])
                elif stack_member[neighbor]:
                    low_link[v] = min(low_link[v], visited[neighbor])

            if low_link[v] == visited[v]:
                scc = []
                while True:
                    node = stack.pop()
                    stack_member[node] = False
                    scc.append(node)
                    if node == v:
                        break
                result.append(scc)

        for v in range(self.V):
            if visited[v] == -1:
                strong_connect(v)

        return result


# Example usage
g = Graph(5)
g.add_edge(1, 0)
g.add_edge(0, 2)
g.add_edge(2, 1)
g.add_edge(0, 3)
g.add_edge(3, 4)

print("Strongly Connected Components:")
scc = g.tarjan_scc()
for component in scc:
    print(component)
