# x is global

x = 1
print(x, "- before sub")

def f():
    #print(x, "- inside before declaration")  # UnboundLocalError
    x = 2
    print(x, "- inside sub")

print(x, "- after sub declaration")

f()

print(x, "- after calling sub")

# 1 - before sub
# 1 - after sub declaration
# 2 - inside sub
# 1 - after calling sub
