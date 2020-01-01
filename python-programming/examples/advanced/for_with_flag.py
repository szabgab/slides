names = ['Foo', 'Bar', 'Baz']

ok = False
for i in range(3):
    name = raw_input('Your name please: ')
    if name in names:
        ok = True
        break

if not ok:
    print("Not OK")
    exit()

print("OK....")


