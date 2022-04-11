import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(10)

def recursion(n):
    print(f"In recursion {n}")
    recursion(n+1)

recursion(1)
