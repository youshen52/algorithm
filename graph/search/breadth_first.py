from collections import deque


def breadth_first_search(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        current_node = queue.popleft()

        if current_node not in visited:
            visited.add(current_node)

            for neighbor in graph[current_node]:
                queue.append(neighbor)

    return visited
