import time


def replace(func):
    def new_func():
        print("start new")
        start = time.time()
        func()
        end = time.time()
        print(f"end new {end-start}")
    return new_func

@replace
def f():
    time.sleep(1)
    print("in f")


f()


