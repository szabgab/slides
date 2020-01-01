import sys
from contextlib import contextmanager

if len(sys.argv) < 3:
    exit(f"Usage: {sys.argv[0]} OUTFILE INFILEs")

outfile = sys.argv[1]
infiles = sys.argv[2:]
#print(outfile)
#print(infiles)

@contextmanager
def myopen(outfile, *infiles):
    #print(len(infiles))
    out = open(outfile, 'w')
    ins = []
    for filename in infiles:
        ins.append(open(filename, 'r'))
    try:
        yield out, ins
    except Exception as ex:
        print(ex)
        pass
    finally:
        out.close()
        for fh in ins:
            fh.close()


with myopen(outfile, *infiles) as (out, input_fhs):
    #print(out.__class__.__name__)
    #print(len(input_fhs))
    while True:
        row = ''
        done = False
        for infh in (input_fhs):
            line = infh.readline()
            #print(f"'{line}'")
            if not line:
                done = True
                break
            if row:
                row += ','
            row += line.rstrip("\n")
        if done:
            break
        out.write(row)
        out.write("\n")

