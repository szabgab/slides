v1 = ['foo', 'bar', 'baz']
v2 = 'abc'

result = map(lambda x,y: x+y, v1, v2)
print(result)
print( list(result) )
