import re, json, os

def fix(s):
    return re.sub(r'(\s)([^:\s][^:]+[^:\s])(\s+:)', r'\1"\2"\3', s)

json_file = os.path.join(
    os.path.dirname(__file__),
    'bad.json'
)
with open(json_file) as fh:
    bad_json_rows = fh.readlines()
    json_str = ''.join(map(fix, bad_json_rows))
    print(json_str)
    data = json.loads(json_str)
    print(data)


