import hashlib
import sys


def gravatar(email):
    return hashlib.md5(email.strip().lower().encode('utf8')).hexdigest()

if len(sys.argv) != 2:
    exit(f"Usage: {sys.argv[0]} EMAIL")

email = sys.argv[1]
code = gravatar(email)
print(f"https://www.gravatar.com/avatar/{code}?s=100&d=blank")

