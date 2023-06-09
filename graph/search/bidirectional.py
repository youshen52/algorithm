def bidirectional_search(graph, start, goal):
    forward_queue = [start]
    backward_queue = [goal]
    forward_visited = set()
    backward_visited = set()

    while forward_queue and backward_queue:
        forward_node = forward_queue.pop(0)
        backward_node = backward_queue.pop(0)

        if forward_node in backward_visited or backward_node in forward_visited:
            return True

        if forward_node not in forward_visited:
            forward_visited.add(forward_node)
            forward_queue.extend(graph[forward_node])

        if backward_node not in backward_visited:
            backward_visited.add(backward_node)
            backward_queue.extend(graph[backward_node])

    return False
