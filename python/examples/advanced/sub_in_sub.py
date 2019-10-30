
def f():
    print("in f")
    def g():
       print("in g")
    g()

f()
#g()  # does not exist here

