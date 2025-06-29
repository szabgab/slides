import sys

files = sys.argv[1:]

fhs = {}
rows = {}
for filename in files:
    try:
        fhs[filename] = open(filename)
        rows[filename] = None
    except Exception:
        print("Could not open {filename}")


while True:
    files_with_content = []
    for filename, fh in fhs.items():
        if rows[filename] is None:
            rows[filename] = fh.readline()
        if rows[filename] != '':
            files_with_content.append(filename)

    if not files_with_content:
        break

    sorted_rows = sorted(files_with_content, key=lambda filename: rows[filename].split(',')[0])
    smallest = sorted_rows[0]
    print(rows[smallest], end='')
    rows[smallest] = None


for fh in fhs.values():
    fh.close()

