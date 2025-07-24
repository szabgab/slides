a = "2.1"
b = float(a)
c = int(b)
print(c)                   # 2
print( type(a) )           # <class 'str'>
print( type(b) )           # <class 'float'>
print( type(c) )           # <class 'int'>

d = int( float(a) )
print(d)                   # 2
print( type(d) )           # <class 'int'>

print( int( float(2.1) ))  # 2
print( int( float("2") ))  # 2
print( int( float(2) ))    # 2
