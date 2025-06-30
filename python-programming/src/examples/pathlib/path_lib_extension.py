from pathlib import Path

file = Path("path/to/code.py")
print(file.suffix)  # .py
print(file.suffix.__class__.__name__)  # str

file = Path("path/to/code.yaml")
print(file.suffix)   # .yaml

file = Path("path/to/.bashrc")
print(file.suffix)   # (empty string)

folder = Path("path/to")
print(folder.suffix) #  (empty string)

