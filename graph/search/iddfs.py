def iterative_deepening_dfs(graph, start, goal, depth_limit):
    for depth in range(depth_limit):
        visited = set()
        if dfs(graph, start, goal, depth, visited):
            return True

    return False


def dfs(graph, current, goal, depth, visited):
    if current == goal:
        return True

    if depth == 0:
        return False

    visited.add(current)

    for neighbor in graph[current]:
        if neighbor not in visited:
            if dfs(graph, neighbor, goal, depth - 1, visited):
                return True

    visited.remove(current)
    return False
