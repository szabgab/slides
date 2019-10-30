def f():
    global x
    # print(x)  # NameError
    x = 2
    print(x, "- inside sub")

# print(x, " - after sub declaration")  # NameError

f()

print(x, "- after calling sub")

# 2 - inside sub
# 2 - after calling sub
