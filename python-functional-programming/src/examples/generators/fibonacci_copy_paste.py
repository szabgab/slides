def fibonacci():
    a, b = 0, 1
    while True:
        a, b = b, a+b

        print(a)
        if a % 17 == 0:
            print('found')
            break

        if a > 200:
            print('not found')
            break

fibonacci()
