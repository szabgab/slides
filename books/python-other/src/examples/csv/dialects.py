import csv

for dialect_name in csv.list_dialects():
    print(dialect_name)
    dialect = csv.get_dialect(dialect_name)
    for attribute_name in [
            'delimiter',
            'doublequote',
            'escapechar',
            'lineterminator',
            'quotechar',
            'quoting',
            'skipinitialspace',
            'strict',
        ]:
        attr = getattr(dialect, attribute_name)
        if attr == '\t':
            attr = '\\t'
        if attr == '\r\n':
            attr = '\\r\\n'
        print("  {:16} '{}'".format(attribute_name, attr))

