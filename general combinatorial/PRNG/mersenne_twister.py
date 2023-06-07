class MersenneTwister:
    def __init__(self, seed=5489):
        self.index = 0
        self.MT = [0] * 624
        self.MT[0] = seed

        for i in range(1, 624):
            self.MT[i] = (
                1812433253 * (self.MT[i - 1] ^ (self.MT[i - 1] >> 30)) + i
            ) & 0xFFFFFFFF

    def extract_number(self):
        if self.index == 0:
            self.generate_numbers()

        y = self.MT[self.index]
        y ^= y >> 11
        y ^= (y << 7) & 0x9D2C5680
        y ^= (y << 15) & 0xEFC60000
        y ^= y >> 18

        self.index = (self.index + 1) % 624
        return y

    def generate_numbers(self):
        for i in range(624):
            y = (self.MT[i] & 0x80000000) + (self.MT[(i + 1) % 624] & 0x7FFFFFFF)
            self.MT[i] = self.MT[(i + 397) % 624] ^ (y >> 1)

            if y % 2 != 0:
                self.MT[i] ^= 0x9908B0DF


# Usage example
mt = MersenneTwister(seed=1234)
for i in range(20):
    random_number = mt.extract_number()
    print(random_number)
