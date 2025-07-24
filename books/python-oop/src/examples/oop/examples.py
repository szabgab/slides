
# numbers
print((255).bit_length())    # 8
print((256).bit_length())    # 9
x = 255
print(x.bit_length())
x = 256
print(x.bit_length())

# strings
print( "hello WOrld".capitalize() )  # Hello world
print( ":".join(["a", "b", "c"]) )   # a:b:c


# lists
numbers = [2, 17, 4]
print(numbers)        # [2, 17, 4]

numbers.append(7)
print(numbers)        # [2, 17, 4, 7]

numbers.sort()
print(numbers)        # [2, 4, 7, 17]

