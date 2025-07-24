from passlib.hash import pbkdf2_sha256
import sys

if len(sys.argv) != 2:
   exit("Usage: {} PASSWORD".format(sys.argv[0]))

pw = sys.argv[1]

hash1 = pbkdf2_sha256.hash(pw)
print(hash1)

hash2 = pbkdf2_sha256.hash(pw)
print(hash2)

print(pbkdf2_sha256.verify(pw, hash1))
print(pbkdf2_sha256.verify(pw, hash2))

