# http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python

# Create a new-style class
class A(object):
    pass
print(type(A))        # <type 'type'>
a = A()
print(type(a))        # <class '__main__.A'>

B = type('B', (), {})
print(type(B))        # <type 'type'>
b = B()
print(type(b))        # <class '__main__.B'>

# old style
class C():
    pass
print(type(C))       # <type 'classobj'>
c = C()
print(type(c))       # <type 'instance'>

# Have attributes in the class
class AA(object):
    name = 'Foo'
print(AA.name)   # Foo
aa = AA()
print(aa.name)   # Foo


BB = type('BB', (), {'name' : 'Bar'})
print(BB.name)   # Bar
bb = BB()
print(bb.name)   # Bar


# Intherit from a class
class AAA(AA):
    pass
print(AAA.name) # Foo
aaa = AAA()
print(aaa.name) # Foo

BBB = type('BBB', (BB,), {})
print(BB.name)  # Bar
bbb = BBB()
print(bbb.name) # Bar


def f(self):
    print(self.name)

class AAAA(object):
    name = 'AAAA-Foo'
    def show(self):
        print(self.name)

aaaa = AAAA()
aaaa.show() # AAAA-Foo

BBBB = type('BBBB', (), { 'name': 'BBBB-Bar', 'show' : f})
bbbb = BBBB()
bbbb.show() # BBBB-Bar
