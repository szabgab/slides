def main():
    a = input("First number: ")
    b = input("Second number: ")

    if int(a) == int(b):
        print("They are equal")
    elif int(a) < int(b):
        print(f"{a} is smaller than {b}")
    else:
        print(f"{a} is bigger than {b}")


main()
