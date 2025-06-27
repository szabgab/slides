a_in = input("Please type in a whole number: ")
b_in = input("Please type in another whole number: ")

if not a_in.isdecimal():
    exit("First input was not a whole number")
if not b_in.isdecimal():
    exit("Second input was not a whole number")


a_num = float(a_in)
b_num = float(b_in)

if a_num > b_num:
    print("First number is bigger")
elif a_num < b_num:
    print("First number is smaller")
else:
    print("They are equal")
