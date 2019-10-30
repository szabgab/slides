import inspect
import sys

level = int(sys.argv[1])


def f():
    print("in f before g")
    g()
    print("in f after g")

def g():
    print("in g")
    PrintFrame()


def PrintFrame():
  st = inspect.stack()

  frame = st[level][0]
  info = inspect.getframeinfo(frame)
  print('__file__:     ', info.filename)
  print('__line__:     ', info.lineno)
  print('__function__: ', info.function)

  print('* file', st[level][1])
  print('* line', st[level][2])
  print('* sub',  st[level][3])

f()

