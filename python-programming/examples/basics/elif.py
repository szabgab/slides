def main():
    a = input('First number: ')
    b = input('Second number: ')

    if a == b:
        print('They are equal')
    elif int(a) < int(b):
        print(a + ' is smaller than ' + b)
    else:
        print(a + ' is bigger than ' + b)


main()
