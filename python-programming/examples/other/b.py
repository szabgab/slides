def main():
    x = "The black cat climbed the green tree."
    n = 0
    while True:
        range1 = x.find("c",n)
        if range1 == -1:
            break
        else:
            print(range1)
            n = n + 1

main()

