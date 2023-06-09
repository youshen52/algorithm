class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.children = []


def find_lca(root, u, v):
    def make_set(x):
        x.parent = x

    def find(x):
        if x.parent == x:
            return x
        x.parent = find(x.parent)
        return x.parent

    def union(x, y):
        x_root = find(x)
        y_root = find(y)
        y_root.parent = x_root

    def dfs(node, ancestors):
        make_set(node)
        ancestors[find(node)] = node
        for child in node.children:
            dfs(child, ancestors)
            union(node, child)
            ancestors[find(node)] = node

    ancestors = {}
    dfs(root, ancestors)
    if u not in ancestors or v not in ancestors:
        return None
    while u != v:
        if u in ancestors:
            u = ancestors[u]
        else:
            u = None
        if v in ancestors:
            v = ancestors[v]
        else:
            v = None
    return u


# Example usage:
root = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
root.children = [node2, node3]
node2.children = [node4]
node3.children = [node5]
print("Lowest Common Ancestor:", find_lca(root, node4, node5).key)
