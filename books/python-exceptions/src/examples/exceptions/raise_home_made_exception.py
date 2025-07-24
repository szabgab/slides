class MyException(Exception):
    def __init__(self, name, address):
        self.name  = name
        self.address = address
    def __str__(self):
        return f'Have you encountered problems? name:{self.name}  address:{self.address}'


def some():
    raise MyException(name = "Foo Bar", address = "Somewhere deep in the code")

def main():
    try:
        some()
    except MyException as err:
        print(err.name)
        print(err.address)

        print(err)
        print("Type: " + type(err).__name__)
    except Exception as err:
        print(f"Some other issue {err}")

main()

# Foo Bar
# Somewhere deep in the code
# Have you encountered problems? name:Foo Bar  address:Somewhere deep in the code
# Type: MyException
