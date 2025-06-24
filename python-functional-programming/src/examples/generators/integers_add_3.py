from series import integers

n3  = (n+3 for n in integers())
# n3 = integers(3)
for i in n3:
    print(i)
    if i >= 10:
        break
