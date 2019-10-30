def create():
    def func():
        func.cnt += 1
        return func.cnt
    func.cnt = 0
    return func

a = create()
b = create()
print(a())    # 1
print(a())    # 2
print(b())    # 1
print(a())    # 3

b.cnt = 7
print(a.cnt)  # 3
print(b.cnt)  # 7

