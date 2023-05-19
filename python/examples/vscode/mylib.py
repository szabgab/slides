import random

def count():
    for x in range(1000):
        v = random.choice("abcd")
        print(x)
        print(v)

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y


def calc(x, y, z):
    if z == "+":
        return x + y
    if z == "*":
        return x * y
    if z == "-":
        return x - y
    if z == "/":
        return x / y
    raise Exception(f"Unknown operator {z}")

