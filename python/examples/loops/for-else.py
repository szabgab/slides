found_number_bigger_than_10 = False

numbers = [2, 3, 4]
for num in numbers:
    if num > 10:
        found_number_bigger_than_10 = True
        break
    print(num)

if found_number_bigger_than_10:
    print("found number bigger than 10")

print('---------------------')

found_number_bigger_than_10 = False

numbers = [2, 3, 12, 4]
for num in numbers:
    if num > 10:
        found_number_bigger_than_10 = True
        break
    print(num)

if found_number_bigger_than_10:
    print("found number bigger than 10")

print('---------------------')



for num in [2, 3, 4]:
    if num > 10:
        break
    print(num)
else:
    print("in else - finished without calling break")
    print("not found number bigger than 10")

print('---------------------')

for num in [2, 3, 12, 4]:
    if num > 10:
        break
    print(num)
else:
    print("in else - finished after calling break")
    print("not found number bigger than 10")

