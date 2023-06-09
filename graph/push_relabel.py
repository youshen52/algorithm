class PushRelabel:
    def __init__(self, graph, source, sink):
        self.graph = graph
        self.source = source
        self.sink = sink
        self.num_nodes = len(graph)
        self.height = [0] * self.num_nodes
        self.excess_flow = [0] * self.num_nodes
        self.flow = [[0] * self.num_nodes for _ in range(self.num_nodes)]

        self.height[source] = self.num_nodes

        for neighbor, capacity in self.graph[source].items():
            self.flow[source][neighbor] = capacity
            self.flow[neighbor][source] = -capacity
            self.excess_flow[neighbor] = capacity
            self.excess_flow[source] -= capacity

    def push(self, u, v):
        flow_increase = min(self.excess_flow[u], self.graph[u][v] - self.flow[u][v])
        self.flow[u][v] += flow_increase
        self.flow[v][u] -= flow_increase
        self.excess_flow[u] -= flow_increase
        self.excess_flow[v] += flow_increase

    def relabel(self, u):
        min_height = float("inf")
        for neighbor in self.graph[u]:
            if self.graph[u][neighbor] - self.flow[u][neighbor] > 0:
                min_height = min(min_height, self.height[neighbor])
                self.height[u] = min_height + 1

    def discharge(self, u):
        while self.excess_flow[u] > 0:
            if len(self.graph[u]) == 0:
                self.relabel(u)
                break

            for neighbor in self.graph[u]:
                if (
                    self.graph[u][neighbor] - self.flow[u][neighbor] > 0
                    and self.height[u] == self.height[neighbor] + 1
                ):
                    self.push(u, neighbor)
                    if self.excess_flow[u] == 0:
                        break

            if self.excess_flow[u] > 0:
                self.relabel(u)

    def max_flow(self):
        for node in self.graph:
            for neighbor in self.graph[node]:
                if neighbor not in self.graph:
                    self.graph[neighbor] = {}

        for node in self.graph:
            for neighbor in self.graph[node]:
                if neighbor not in self.flow:
                    self.flow[neighbor] = {}

        for node in self.graph:
            for neighbor in self.graph[node]:
                self.flow[node][neighbor] = 0
                self.flow[neighbor][node] = 0

        active_nodes = [
            node for node in self.graph if node != self.source and node != self.sink
        ]

        while active_nodes:
            u = active_nodes[0]
            old_height = self.height[u]
            self.discharge(u)
            if self.height[u] > old_height:
                active_nodes.remove(u)
                active_nodes.insert(0, u)

        max_flow = 0
        for neighbor, flow in self.flow[self.source].items():
            max_flow += flow

        return max_flow
