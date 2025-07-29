def create_function():
    print("creating a function")
    def internal():
        print("This is the generated function")
    print("creation done")
    return internal

func = create_function()

func()



