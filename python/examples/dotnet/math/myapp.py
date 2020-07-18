import clr
dll = clr.FindAssembly('MyMath')  # returns path to dll
assembly = clr.AddReference('MyMath')
#print(type(assembly)) # <class 'System.Reflection.RuntimeAssembly'>
#print(dir(assembly))
from MyMath import MyMathClass
from MyMath import MyMathClass as My


assert My.addInts(2, 3)         == 5
assert My.addInts(2.7, 7.8)     == 9
assert My.addDouble(11.2, 23.3) == 34.5
assert My.addString("hello", "world") == "hello world"

assert My.andBool(1, 1) is True
assert My.andBool(1, 0) is False
assert My.andBool(True, True) is True
assert My.andBool(False, True) is False

assert My.str_by_index(["apple", "banana", "peach"], 0) == "apple"
assert My.str_by_index(["apple", "banana", "peach"], 1) == "banana"
assert My.int_by_index([17, 19, 42], 1) == 19
# Mixed list cannot be passed

# tuple can be passed
assert My.int_by_index((17, 21, 42), 2) == 42

# TODO: string, char, float
# TODO strings, lists, dicts,
# TODO complex data structures in C#
# TODO Async