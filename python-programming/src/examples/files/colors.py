def main():
    try:
        with open('colors.txt') as fh:
            colors = []
            for line in fh:
                colors.append(line.rstrip("\n"))
    except IOError:
        print("Could not open colors.txt")
        exit()

    for i in range(len(colors)):
        print("{}) {}".format(i, colors[i]))

    c = int(input("Select color: "))
    print(colors[c])

main()
