import requests
from ptpython.repl import embed

res = requests.get("https://code-maven.com/")
embed(globals(), locals())

print("done")
