from warnings import warn

def foo():
    warn("foo will be deprecated soon. Use bar() instead", DeprecationWarning)
    print("foo still works")


def main():
    foo()
    print("afterfoo")

main()
