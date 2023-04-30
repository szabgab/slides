import sys
import string
import random


def main():
    if len(sys.argv) != 3:
        exit(f"Usage: {sys.argv[0]} NUMBER_OF_FILES   NUMBER_OF_ROWS")
    number_of_files = int(sys.argv[1])
    number_of_rows = int(sys.argv[2])
    characters = string.ascii_letters + ' ' + string.digits
    print(number_of_rows)
    for file_id in range(1, number_of_files + 1):
        filename = f"{file_id}.txt"
        print(filename)
        with open(filename, "w") as fh:
            for _ in range(number_of_rows):
                length = random.randrange(0, 81)
                print(length)
                row = ''.join(random.choices(characters, k=length))
                fh.write(row + "\n")

if __name__ == "__main__":
    main()
