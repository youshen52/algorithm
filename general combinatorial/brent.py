def brent_algorithm(f, x0):
    # Main phase of algorithm: search for a repetition x_i = x_2i
    power = lam = 1
    tortoise = x0
    hare = f(x0)  # f(x0) is the element/node next to x0.
    while tortoise != hare:
        if power == lam:  # Time to start a new power of two?
            tortoise = hare
            power *= 2
            lam = 0
        hare = f(hare)
        lam += 1

    # Find the position of the first repetition of length λ
    mu = 0
    tortoise = hare = x0
    for _ in range(lam):
        hare = f(hare)

    # Find the length of the shortest cycle starting from x_μ
    length = 1
    hare = f(tortoise)
    while tortoise != hare:
        hare = f(hare)
        length += 1

    return length
