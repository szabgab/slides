import sys

def main():
    if len(sys.argv) != 4:
        exit(f"Usage: {sys.argv[0]} IN_FILE IN_FILE OUT_FILE")
    infile_a, infile_b = sys.argv[1:3]
    outfile = sys.argv[3]

    with open(outfile, 'w') as out_fh, open(infile_a) as in_a, open(infile_b) as in_b:
        cnt = 0
        for lines in zip(in_a, in_b):
            #print(lines)
            lines = list(map(lambda s: s.rstrip('\n'), lines))
            #print(lines)
            if lines[0] != lines[1]:
                out_fh.write(f"{cnt},{lines[0]},{lines[1]}\n")
            cnt += 1

main()
