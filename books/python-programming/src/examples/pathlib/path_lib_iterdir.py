from pathlib import Path

folder = Path(".")

for item in folder.iterdir():
    print(item)
