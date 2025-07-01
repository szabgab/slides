import argparse

def is_age(age: str) -> float:
    try:
        new_age = float(age)
    except ValueError:
        raise argparse.ArgumentTypeError(f"This: {age!r} is not a valid number.")

    if new_age < 0:
        raise argparse.ArgumentTypeError(f"It must be a non-negative number. We received {age!r} ")

    return new_age

parser = argparse.ArgumentParser()
parser.add_argument("--age", type=is_age, required=True)

args = parser.parse_args()
print(args.age)
