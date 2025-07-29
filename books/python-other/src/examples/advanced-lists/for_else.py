names = ['Foo', 'Bar', 'Baz']


for i in range(3):
    name = input('Your name please: ')
    if name in names:
        break
else:
    print("Not OK")
    exit()

print("OK....")
