def read_and_divide(filename):
    print("before " + filename)
    with open(filename, 'r') as fh:
        number = int(fh.readline())
        print(100 / number)
    print("after  " + filename)
