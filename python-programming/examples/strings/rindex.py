text = "The black cat climbed the green tree."
print(text.rindex("c"))         # 14
print(text.rindex("c", 8))      # 14
print(text.rindex("c", 8, 13))  # 10

print(text.rindex("gr", 8))     # 26
print(text.rindex("gr", 8, 16))


