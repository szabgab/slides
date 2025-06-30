from pathlib import Path

this = Path(__file__)
print(this)
print(this.parts[-1]) # (basename)
print(this.parts[0])  # /
print(this.parts)     # (each part of the path)

