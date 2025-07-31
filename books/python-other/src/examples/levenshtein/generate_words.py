import sys
import random
import string

# TODO: set min, max word length
# TODO: set filename
# TODO: set character types
# TODO: allow spaces?

def main():
    filename = "words.txt"
    min_len  = 6
    max_len  = 6

    if len(sys.argv) != 2:
        exit(f"Usage: {sys.argv[0]} WORD_COUNT")
    count = int(sys.argv[1])
    with open(filename, 'w') as fh:
        for _ in range(count):
            word = ''
            length = random.randrange(min_len, max_len+1)
            for _ in range(length):
                word += random.choice(string.ascii_lowercase)
            fh.write(word + "\n")

main()
