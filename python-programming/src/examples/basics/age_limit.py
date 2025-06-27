age = float(input('Please type in your age: '))
if 21 <= age:
    print('You can already drink alcohol. In the USA as well.')
elif 18 <= age:
    print('You can already drink alcohol. (But not in the USA.)')
else:
    print('You cannot legally drink alcohol.')
