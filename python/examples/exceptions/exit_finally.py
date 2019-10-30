
def f():
    try:
        return
    finally:
       print("finally in f")

def g():
    try:
        exit()
    finally:
       print("finally in g")

print("before")
f()
print("after f")
g()
print("after g")

# before
# finally in f
# after f
# finally in g
