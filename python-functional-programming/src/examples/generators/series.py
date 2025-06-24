def integers(n = 1):
   while True:
       yield n
       n += 1

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


def gfibonacci(size = 2):
    """Generalized Fibonacci. """
    values = [0]
    while True:
        yield values[-1]
        if len(values) < size:
            values.append(1)
        else:
            values.append(sum(values))
            values = values[1:]

def pascal():
    values = [1]
    while True:
        yield values
        new = [1]
        for i in range(0, len(values)-1):
            new.append(values[i] + values[i+1])
        new.append(1)
        values = new
