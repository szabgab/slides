import sys
import pylev

def main():
    if len(sys.argv) != 2:
        exit(f"Usage: {sys.argv[0]} filename")
    filename = sys.argv[1]
    outfile = 'out.txt'

    rows = []
    with open(filename) as fh:
        for row in fh:
            rows.append(row.rstrip("\n"))
    with open(outfile, 'w') as fh:
        for a in rows:
            for b in rows:
                dist = pylev.levenshtein(a, b)
                fh.write(f"{a},{b},{dist}\n")

main()
