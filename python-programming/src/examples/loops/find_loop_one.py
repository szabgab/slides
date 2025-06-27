text = "The black cat climbed the green tree."
loc = -1
while True:
    loc = text.find("c", loc+1)
    if loc == -1:
        break
    print(loc)
