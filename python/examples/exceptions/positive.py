def positive(num):
   if type(num).__name__ == 'float':
       raise Exception("The given parameter {} is a float and not an int.".format(num))

   if type(num).__name__ != 'int':
       raise Exception("The given parameter {} is of type {} and not int.".format(num, type(num).__name__))

   if num < 0:
       raise Exception("The given number {} is not positive.".format(num))

for val in [14, 24.3, "hi", -10]:
   print(val)
   print(type(val).__name__)
   try:
       positive(val)
   except Exception as ex:
       print("Exception: {}".format(ex))
