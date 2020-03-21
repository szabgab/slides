a_in = input("Please type in a string: ")
b_in = input("Please type in another string: ")
print("How to compare:")
print("1) ASCII")
print("2) Length")
how = input()

if how == '1':
    first = a_in > b_in
    second = a_in < b_in
elif how == '2':
    first = len(a_in) > len(b_in)
    second = len(a_in) < len(b_in)

if first:
    print("First number is bigger")
elif second:
    print("First number is smaller")
else:
    print("They are equal")
