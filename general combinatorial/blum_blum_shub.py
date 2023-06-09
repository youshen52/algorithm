class BBSGenerator:
    def __init__(self, p, q, seed):
        self.p = p
        self.q = q
        self.n = p * q
        self.state = seed

    def next(self):
        self.state = (self.state * self.state) % self.n
        return self.state % 2


# Usage
bbs = BBSGenerator(p=7, q=11, seed=123)
print(bbs.next())
