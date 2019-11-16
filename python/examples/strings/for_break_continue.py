txt = "The black cat climbed the green tree."

for c in txt:
    if c == ' ':
        continue
    if c == 't':
        break
    print(c)

