from pathlib import Path

cwd = Path.cwd()
print(cwd)
print(cwd.__class__.__name__)  # PosixPath

