def my_exit(code: str | int):
    print(type(code).__name__)

my_exit(3)
my_exit("problem")
my_exit(3.14)
