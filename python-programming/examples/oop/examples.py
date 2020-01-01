
# numbers
num = 255
print(num.bit_length())    # 8
num = 256
print(num.bit_length())    #  9

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

