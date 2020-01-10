import clr
dll = clr.FindAssembly('MyMath')  # returns path to dll
assembly = clr.AddReference('MyMath')
#print(type(assembly)) # <class 'System.Reflection.RuntimeAssembly'>
#print(dir(assembly))
from MyMath import MyMathClass
print(MyMathClass.addInts(2, 3))
