def some():
    raise Exception("Some Error")

def main():
    try:
        some()
    except Exception as err:
        print(err)
        print("Type: " + type(err).__name__)

main()

# Some Error
# Type: Exception
