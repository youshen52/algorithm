def prufer_to_tree(prufer):
    n = len(prufer) + 2
    degree = [1] * n
    tree = []

    for i in prufer:
        degree[i] += 1

    j = 0
    while degree[j] != 1:
        j += 1

    leaf = j
    for vertex in prufer:
        tree.append((leaf, vertex))
        degree[leaf] -= 1
        degree[vertex] -= 1
        if degree[vertex] == 1 and vertex < j:
            leaf = vertex
        else:
            j += 1
            while degree[j] != 1:
                j += 1
            leaf = j

    for i in range(1, n - 1):
        if degree[i] == 1:
            tree.append((i, n - 1))
            break

    return tree


def tree_to_prufer(tree):
    n = len(tree) + 2
    degree = [1] * n
    prufer = []

    for edge in tree:
        u, v = edge
        degree[u] += 1
        degree[v] += 1

    for _ in range(n - 2):
        leaf = min(i for i in range(n) if degree[i] == 1)
        neighbor = min(v for v in range(n) if degree[v] == 1 and v != leaf)
        prufer.append(neighbor)
        degree[leaf] -= 1
        degree[neighbor] -= 1

    return prufer


# Example usage:
prufer_sequence = [4, 2, 3, 3]
tree = prufer_to_tree(prufer_sequence)
print("Tree:", tree)
prufer = tree_to_prufer(tree)
print("Prüfer Sequence:", prufer)
