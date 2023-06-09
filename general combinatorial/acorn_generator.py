class ACORNGenerator:
    def __init__(self, seed):
        self.state = seed

    def next(self):
        self.state ^= self.state >> 7
        self.state ^= self.state << 9
        self.state ^= self.state >> 13
        return self.state


# Usage
acorn = ACORNGenerator(seed=123)
print(acorn.next())
