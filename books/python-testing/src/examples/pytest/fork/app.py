import os

def func(x, y):
    pid = os.fork()
    if pid == 0:
        print(f"Child {os.getpid()}")
        #raise Exception("hello")
        exit()
    print(f"Parent {os.getpid()} The child is {pid}")
    os.wait()
    #exit()
    #raise Exception("hello")
    return x+y
  

if __name__ == '__main__':
    func(2, 3)
