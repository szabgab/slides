class MyError(Exception):
    pass

try:
    raise(MyError('hello', 'world'))
except Exception as e:
    print(type(e))
    print(e)
    print(e.args)

