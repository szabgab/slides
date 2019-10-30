a = "The black cat climbed the green tree."
print(a.find("bl"))     # 4
print(a.find("The"))    # 0
print(a.find("dog"))    # -1

print(a.find("c"))      # 7
print(a.find("c", 8))   # 10

print(a.find("gr", 8))      # 26
print(a.find("gr", 8, 16))  # -1
