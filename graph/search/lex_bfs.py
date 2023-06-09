from collections import deque


def lexicographic_bfs(graph):
    ordering = []
    queue = deque([list(graph.keys())[0]])

    while queue:
        current_node = queue.popleft()
        ordering.append(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in ordering and neighbor not in queue:
                queue.append(neighbor)

    return ordering
