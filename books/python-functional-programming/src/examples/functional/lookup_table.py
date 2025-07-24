import sys

table = {
    "cat"  : lambda : print("miau"),
    "dog"  : lambda : print("hauhau"),
    "duck" : lambda : print("hap hap"),
}


def main():
    if len(sys.argv) != 2:
        exit(f"Usage: {sys.argv[0]} NAME")

    animal = sys.argv[1]
    if animal in table:
        table[animal]()

main()

