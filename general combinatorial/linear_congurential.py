class LCGGenerator:
    def __init__(self, seed, a, c, m):
        self.state = seed
        self.a = a
        self.c = c
        self.m = m

    def next(self):
        self.state = (self.a * self.state + self.c) % self.m
        return self.state


# Usage
lcg = LCGGenerator(seed=123, a=1103515245, c=12345, m=2**31)
print(lcg.next())
