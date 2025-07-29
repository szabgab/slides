def f():
    def g():
        print("in g")
    print("start f")
    g()
    print("end f")

f()
g()
