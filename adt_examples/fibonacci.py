class Fib:
    def __init__(self):
        self.num1 = 0
        self.num2 = 1

    def __iter__(self):
        return self

    def __next__(self):
        val = self.num1 + self.num2
        self.num1, self.num2 = self.num2, val
        return val
