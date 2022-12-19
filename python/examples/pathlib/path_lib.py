from pathlib import Path

this = Path(__file__)
print(this)
print(this.parent)
print(this.parents[1])

print(list(this.parent.iterdir()))
# .exists
# joinpath or /
# mkdir()
# Path.cwd()
