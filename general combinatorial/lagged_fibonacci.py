class LaggedFibonacciGenerator:
    def __init__(self, k, seed):
        self.k = k
        self.state = [seed] * k

    def next(self):
        next_value = (self.state[-self.k] + self.state[-1]) % (2**32)
        self.state.append(next_value)
        return next_value


# Usage
lfib = LaggedFibonacciGenerator(k=3, seed=123)
print(lfib.next())
