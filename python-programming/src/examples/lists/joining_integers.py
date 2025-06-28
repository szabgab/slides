a = ["x", "2", "y"]
b = ["x", 2, "y"]
print(":".join(a))    # x:2:y
# print ":".join(b)    # TypeError: sequence item 1: expected string, int found

# convert elements to string using map
print(":".join( map(str, b) ))        # x:2:y


# convert elements to string using list comprehension
print(":".join( str(x) for x in b ))  # x:2:y
