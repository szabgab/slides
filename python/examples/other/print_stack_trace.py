import traceback

def f():
  g()

def g():
    #print(traceback.extract_stack())
    print(''.join(traceback.format_stack()))

f()
print("done")

#https://docs.python.org/3/library/traceback.html
