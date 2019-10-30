fields = ['one', 'two and three', 'four', 'five']

together = ':'.join(fields)
print(together) # one:two and three:four:five

mixed = ' -=<> '.join(fields)
print(mixed) # one -=<> two and three -=<> four -=<> five

another = ''.join(fields)
print(another)  # onetwo and threefourfive
