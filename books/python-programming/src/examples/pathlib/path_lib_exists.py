from pathlib import Path

file = Path(__file__)
print(file.exists())  # True

file = Path("hello.txt")
print(file.exists())  # False


folder = Path(".")
print(folder.exists())  # True
