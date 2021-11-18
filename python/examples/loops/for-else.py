
for num in [2, 3, 4]:
    if num > 10:
        break
    print(num)
else:
    print("in else - finished without calling break")
print('')

for num in [2, 3, 12]:
    if num > 10:
        break
    print(num)
else:
    print("in else - finished after calling break")
