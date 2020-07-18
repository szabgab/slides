filename = "rows.txt"
records  = "records.txt"

with open(filename) as in_fh:
    with open(records, 'w') as out_fh:
        for line in in_fh:
            line = line.rstrip("\n")
            out_fh.write("{:>3}{}".format(len(line), line))
