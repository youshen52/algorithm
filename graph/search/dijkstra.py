import heapq


def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_dist, current_node = heapq.heappop(queue)

        if current_dist > distances[current_node]:
            continue

        for neighbor, neighbor_dist in graph[current_node]:
            distance = current_dist + neighbor_dist

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances
