
a = 2

try:
    a + b
except Exception as e:
    print(type(e))
    print(e)
    print(e.args)

try:
   raise(NameError('something else'))
except Exception as e:
    print(type(e))
    print(e)
    print(e.args)
    
