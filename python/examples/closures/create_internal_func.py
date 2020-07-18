def create_func():
    def internal():
        print("Hello world")
    internal()


func = create_func()
internal()
