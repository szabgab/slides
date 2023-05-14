def calc(x, y, z):
    if z == "+":
        return x + y
    if z == "*":
        return x * y
    if z == "-":
        return x - y
    if z == "/":
        return x / y
    raise Exception("Unknown operator {z}")


if __name__ == "__main__":
    print(calc( 2, 3, "+"))
    print(calc( 2, 3, "*"))
