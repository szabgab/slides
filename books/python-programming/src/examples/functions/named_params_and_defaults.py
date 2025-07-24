def f(a, b=2, c=3):
    print(a, b , c)

f(1)             # 1 2 3
f(1, b=0)        # 1 0 3
f(1, c=0)        # 1 2 0
f(1, c=0, b=5)   # 1 5 0

# f(b=0, 1)
# would generate:
# SyntaxError: non-keyword arg after keyword arg

f(b=0, a=1)      # 1 0 3

