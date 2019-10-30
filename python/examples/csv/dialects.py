import csv

for dname in csv.list_dialects():
    print(dname)
    d = csv.get_dialect(dname)
    for n in ['delimiter', 'doublequote', 'escapechar',
            'lineterminator', 'quotechar',
            'quoting', 'skipinitialspace', 'strict']:
        attr = getattr(d, n)
        if attr == '\t':
            attr = '\\t'
        if attr == '\r\n':
            attr = '\\r\\n'
        print("  {:16} '{}'".format(n, attr))

