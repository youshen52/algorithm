import heapq


def best_first_search(graph, start, goal):
    visited = set()
    queue = [(0, start)]

    while queue:
        cost, current_node = heapq.heappop(queue)

        if current_node == goal:
            return True

        if current_node not in visited:
            visited.add(current_node)

            for neighbor, neighbor_cost in graph[current_node]:
                heapq.heappush(queue, (neighbor_cost, neighbor))

    return False
