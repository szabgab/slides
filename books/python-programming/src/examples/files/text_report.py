import sys


def main():
    if len(sys.argv) !=2:
        exit(f"Usage: {sys.argv[0]} FILENAME")
        # text_report.txt

    in_file = sys.argv[1]
    show_rows_with_report(in_file)
    show_rows_start_with_report(in_file)
    show_numbers_after_report(in_file)
    sum_numbers_after_report(in_file)
    sum_numbers_after_report_within_begin_end_section(in_file)


def show_rows_with_report(in_file):
    with open(in_file) as fh:
        for row in fh:
            row = row.rstrip("\n")
            if 'Report:' in row:
                print(row)
    print('-' * 20)

def show_rows_start_with_report(in_file):
    with open(in_file) as fh:
        for row in fh:
            row = row.rstrip("\n")
            if row.startswith('Report:'):
                print(row)
    print('-' * 20)

def show_numbers_after_report(in_file):
    with open(in_file) as fh:
        for row in fh:
            row = row.rstrip("\n")
            if 'Report:' in row:
                parts = row.split(':')
                print(int(parts[1]))
    print('-' * 20)

def sum_numbers_after_report(in_file):
    total = 0
    with open(in_file) as fh:
        for row in fh:
            row = row.rstrip("\n")
            if 'Report:' in row:
                parts = row.split(':')
                total += int(parts[1])
    print(f"Total: {total}")
    print('-' * 20)

def sum_numbers_after_report_within_begin_end_section(in_file):
    in_section = False
    total = 0
    with open(in_file) as fh:
        for row in fh:
            row = row.rstrip("\n")
            if row == 'Begin report':
                in_section = True
                continue
            if row == 'End report':
                in_section = False
                continue
            if in_section:
                if 'Report:' in row:
                    parts = row.split(':')
                    total += int(parts[1])
                    print(int(parts[1]))
    print(f"Total in section: {total}")
    print('-' * 20)


main()

