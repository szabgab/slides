def create_func(name):
    def internal():
        print(f"Hello {name}")

    return internal

foo = create_func("Foo")
foo()


bar = create_func("Bar")
bar()
