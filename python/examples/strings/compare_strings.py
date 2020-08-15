mode = input("Mode of comparision: [length|ascii]")
if mode != "length" and mode != "ascii":
    print("Not good")
    exit()

str1 = input("String 1:")
str2 = input("String 2:")

if mode == "length":
    if len(str1) > len(str2):
        print("First is longer")
    elif len(str1) < len(str2):
        print("Second is longer")
    else:
        print("They are of equal length")
elif mode == "ascii":
    if str1 > str2:
        print("First is later in the ABC order")
    elif str1 < str2:
        print("Second is later in the ABC order")
    else:
        print("The strings are equal")

