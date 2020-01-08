class Fibonacci(object):
    def __init__(self):
        self.values = []

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.values) == 0:
            self.values.append(1)
            return 1

        if len(self.values) == 1:
            self.values.append(1)
            return 1

        self.values.append(self.values[-1] + self.values[-2])
        self.values.pop(0)

        return self.values[-1]
