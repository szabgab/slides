fruits = ['apple', 'banana', 'peach', 'kiwi']

together = ':'.join(fruits)
print(together) # apple:banana:peach:kiwi

together = ' '.join(fruits)
print(together) # apple banana peach kiwi

mixed = ' -=<> '.join(fruits)
print(mixed) # apple -=<> banana -=<> peach -=<> kiwi

another = ''.join(fruits)
print(another)  # applebananapeachkiwi

csv = ','.join(fruits)
print(csv) # apple,banana,peach,kiwi
