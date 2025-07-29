

def call(func):
    return func(42)

def double(val):
    print(2*val)

call(double)      # 84
call(lambda x: print(x // 2))    # 21
