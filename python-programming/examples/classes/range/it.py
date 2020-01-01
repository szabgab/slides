class Range(object):
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):   # Python 3
        return self.next()

    def next(self):       # Python 2
        if self.current >= self.end:
            raise StopIteration
        v = self.current
        self.current += 1
        return v
