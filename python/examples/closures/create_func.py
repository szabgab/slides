def create_func():
    def internal():
        print("Hello world")
    #internal()

    return internal

func = create_func()
#internal()
func()
