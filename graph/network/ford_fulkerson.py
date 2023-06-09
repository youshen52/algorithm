def ford_fulkerson(graph, source, sink):
    def dfs(graph, current, flow, visited):
        visited.add(current)
        if current == sink:
            return flow

        for neighbor, capacity in graph[current].items():
            if neighbor not in visited and capacity > 0:
                min_flow = min(flow, capacity)
                residual_capacity = dfs(graph, neighbor, min_flow, visited)
                if residual_capacity > 0:
                    graph[current][neighbor] -= residual_capacity
                    graph[neighbor][current] += residual_capacity
                    return residual_capacity

        return 0

    max_flow = 0
    while True:
        visited = set()
        flow = dfs(graph, source, float("inf"), visited)
        if flow == 0:
            break
        max_flow += flow

    return max_flow
