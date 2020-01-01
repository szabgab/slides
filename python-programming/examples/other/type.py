x = 2
y = '2'
z = [2, '2']
d = {}

def f():
    pass
l = lambda q: q

class Cold():
    pass
cold = Cold()

class Cnew(object):
    pass
cnew = Cnew()

# r = xrange(10)  # Python 3 does not have xrange

print(type(x))  # <type 'int'>
print(type(y))  # <type 'str'>
print(type(z))  # <type 'list'>
print(type(d))  # <type 'dict'>
print(type(f))  # <type 'function'>
print(type(l))  # <type 'function'>
print(type(Cold))  # <type 'classobj'>
print(type(cold))  # <type 'instance'>
print(type(Cnew))  # <type 'type'>
print(type(cnew))  # <class '__main__.Cnew'>
#print(type(r))  # <type 'xrange'>

print(type(x).__name__)  # int
print(type(y).__name__)  # str
print(type(z).__name__)  # list
