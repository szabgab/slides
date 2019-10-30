def f(a, b = 42):
    print(a)
    print(b)

f(23)
    # 23
    # 42

f(19, 11)
    # 19
    # 11

f(b=7, a=8)
    # 8
    # 7

# f()          # (runtime) TypeError: f() takes at least 1 argument (0 given)
# f(1, 2, 3)   # (runtime) TypeError: f() takes at most 2 arguments (3 given)
# f(b=10, 23)  # SyntaxError: non-keyword arg after keyword arg

# def g(a=23, b):
#     pass
#     SyntaxError: non-default argument follows default argument
