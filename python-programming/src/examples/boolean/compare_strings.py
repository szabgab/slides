a_in = input("Please type in a string: ")
b_in = input("Please type in another string: ")
print("How to compare:")
print("1) ASCII")
print("2) Length")
how = input()

if how == '1':
    first_is_bigger = a_in > b_in
    second_is_bigger = a_in < b_in
elif how == '2':
    first_is_bigger = len(a_in) > len(b_in)
    second_is_bigger = len(a_in) < len(b_in)

if first_is_bigger:
    print("First number is bigger")
elif second_is_bigger:
    print("First number is smaller")
else:
    print("They are equal")
