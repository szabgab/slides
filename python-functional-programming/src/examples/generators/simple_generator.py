def number():
    yield 42
    yield 19
    yield 23

for n in number():
  print(n)
