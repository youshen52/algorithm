def depth_first_search(graph, start, goal):
    visited = set()
    stack = [start]

    while stack:
        current_node = stack.pop()

        if current_node == goal:
            return True

        if current_node not in visited:
            visited.add(current_node)

            for neighbor in graph[current_node]:
                stack.append(neighbor)

    return False
