from pathlib import Path


folder = Path("/")
print(folder)                         # /

subfolder = folder.joinpath("etc")
print(subfolder)                      # /etc

file1 = subfolder.joinpath("a.txt")
print(file1)                          # /etc/a.txt

file2 = subfolder / "b.txt"
print(file2)                          # /etc/b.txt

