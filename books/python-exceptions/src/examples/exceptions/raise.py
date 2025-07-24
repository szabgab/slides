def add_material(name, amount):
    if amount <= 0:
        raise Exception(f"Amount of {name} must be positive. {amount} was given.")
    print(f"Adding {name}: {amount}")

def main():
    things_to_add = (
        ("apple", 3),
        ("sugar", -1),
        ("banana", 2),
    )

    for name, amount in things_to_add:
        try:
            add_material(name, amount)
        except Exception as err:
            print(f"Exception: {err}")
            print("Type: " + type(err).__name__)

main()

