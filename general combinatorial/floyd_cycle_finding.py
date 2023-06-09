def floyd_cycle_finding_algorithm(f, x0):
    tortoise = f(x0)
    hare = f(f(x0))
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(f(hare))

    # Find the position of the first repetition
    mu = 0
    tortoise = x0
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(hare)
        mu += 1

    # Find the length of the shortest cycle
    length = 1
    hare = f(tortoise)
    while tortoise != hare:
        hare = f(hare)
        length += 1

    return length
