def main():
    a = input('First number: ')
    b = input('Second number: ')

    if int(b) == 0:
        print("Cannot divide by 0")
    else:
        print("Dividing", a, "by",  b)
        print(int(a) / int(b))


main()
