text = "The black cat climbed the green tree."
print(text.find("bl"))     # 4
print(text.find("The"))    # 0
print(text.find("dog"))    # -1

print(text.find("c"))      # 7
print(text.find("c", 8))   # 10

print(text.find("gr", 8))      # 26
print(text.find("gr", 8, 16))  # -1


print(text.rfind("c", 8))   # 14
