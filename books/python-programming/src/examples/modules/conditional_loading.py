import random

print("Start running")
name = input("Your name:")

if name == "Foo":
    import mygreet
    mygreet.hello()
else:
    print('No loading')


print("DONE")
