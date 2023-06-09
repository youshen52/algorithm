INF = float("inf")


def hungarian_algorithm(cost_matrix):
    rows = len(cost_matrix)
    cols = len(cost_matrix[0])
    max_match = 0
    match = [-1] * cols
    lx = [max(row) for row in cost_matrix]
    ly = [0] * cols
    slack = [INF] * cols
    slackx = [0] * cols
    prev = [-1] * cols

    def update_labels():
        delta = INF
        for j in range(cols):
            if slack[j] and delta > slack[j]:
                delta = slack[j]
        for i in range(rows):
            if i in S:
                lx[i] -= delta
        for j in range(cols):
            if j not in T:
                ly[j] += delta
            else:
                slack[j] -= delta

    def add_to_tree(x, prevx):
        S.add(x)
        prev[x] = prevx
        for y in range(cols):
            if lx[x] + ly[y] - cost_matrix[x][y] < slack[y]:
                slack[y] = lx[x] + ly[y] - cost_matrix[x][y]
                slackx[y] = x

    def augment():
        while True:
            min_slack = INF
            for j in range(cols):
                if j not in T and slack[j] < min_slack:
                    min_slack = slack[j]
            for i in S:
                lx[i] -= min_slack
            for j in T:
                ly[j] += min_slack
            for j in range(cols):
                if j not in T and slack[j] == 0:
                    if match[j] == -1:
                        y = j
                        x = slackx[j]
                        while True:
                            prev_y = match[y]
                            match[y] = x
                            if prev_y == -1:
                                break
                            x = prev[prev_y]
                            y = prev_y
                        return True
                    else:
                        y = j
                        T.add(y)
                        S.add(match[y])
                        add_to_tree(match[y], slackx[j])
            else:
                update_labels()
                continue
            break
        return False

    for x in range(rows):
        if match[x] == -1:
            S = set()
            T = set()
            slack = [INF] * cols
            slackx = [-1] * cols
            add_to_tree(x, -1)
            if augment():
                max_match += 1

    return max_match


# Example usage:
cost_matrix = [[5, 1, 3], [3, 0, 1], [2, 5, 1]]
print("Perfect Matching:", hungarian_algorithm(cost_matrix))
