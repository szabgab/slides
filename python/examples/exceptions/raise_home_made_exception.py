class MyException(Exception):
    def __init__(self, name, address):
        self.name  = name
        self.address = address
    def __str__(self):
        return 'Have you encountered problems? name:{}  address:{}'.format(self.name, self.address)


def some():
    raise MyException(name = "Foo Bar", address = "Somewhere deep in the code")

def main():
    try:
        some()
    except Exception as err:
        print(err)
        print("Type: " + type(err).__name__)
        print(err.name)
        print(err.address)

main()

# Have you encountered problems? name:Foo Bar  address:Somewhere deep in the code
# Type: MyException
# Foo Bar
# Somewhere deep in the code
