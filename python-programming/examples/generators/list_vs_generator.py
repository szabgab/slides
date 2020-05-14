a_list = [i*2 for i in range(3)]
print(a_list)
for x in a_list:
   print(x)
print()

a_generator = (i*2 for i in range(3))
print(a_generator)
for x in a_generator:
   print(x)

