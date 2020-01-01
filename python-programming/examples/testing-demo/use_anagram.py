from anagram import is_anagram
import sys

if len(sys.argv) != 3:
    exit(f"Usage {sys.argv[0]} WORD WORD")

if is_anagram(sys.argv[1], sys.argv[2]):
    print("Anagram")
else:
    print("NOT")
