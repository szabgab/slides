mode = input("Mode of comparision: [length|ascii|")
if mode != "length" and mode != "ascii":
    print("Not good")
    exit()

str1 = input("String 1:")
str1 = input("String 2:")

if mode == "length":
    print(len(str1) > len(str2))
elif mode == "ascii":
    print(str1 > str2)

