# don't use complex data structures as default values
def extend_and_print(names = []):
    names.append("cat")
    print(names)


extend_and_print()
extend_and_print()
print()

def fixed(names = None):
    if names is None:
        names = []
    names.append("dog")
    print(names)


fixed()
fixed()


