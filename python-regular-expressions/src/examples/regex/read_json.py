import re, json, os

json_file = os.path.join(
    os.path.dirname(__file__),
    'bad.json'
)
with open(json_file) as fh:
    data = json.load(fh)
    # ValueError: Expecting property name: line 2 column 4 (char 5)
