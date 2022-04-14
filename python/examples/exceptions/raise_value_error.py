def div(a, b):
    if b == 0:
        raise ValueError("Cannot divide by 0")
    print(a/b)

def main():
    try:
        div(6, 3)
        div(3, 0)
        div(6, 2)
    except ValueError as err:
        print(f"Exception: {err}")
        print("Type: " + type(err).__name__)

main()

# 2.0
# Exception: Cannot divide by 0
# Type: ValueError

