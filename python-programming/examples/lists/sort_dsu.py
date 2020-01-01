#!/usr/bin/env python

words = ['derf', 'xy', 'abcd', 'dec', 'ab']
print(sorted(words))
     # ['ab', 'abcd', 'dec', 'derf', 'xy']

print(sorted(words, key=len))
     # ['xy', 'ab', 'dec', 'derf', 'abcd']

decorated = [(len(w), w) for w in words]
decorated.sort()
result = [ d[1] for d in decorated]
print(result)
     # ['ab', 'xy', 'dec', 'abcd', 'derf']

print( [ d[1] for d in sorted( [(len(w), w) for w in words] ) ] )
     # ['ab', 'xy', 'dec', 'abcd', 'derf']
