text = "The black cat climbed the green tree."
start = 0
while True:
    loc = text.find("c", start)
    if loc == -1:
        break
    print(loc)
    start = loc + 1
