import sys


def add_grades(filename):
    grades = {}
    with open(filename) as fh:
        for line in fh:
            line = line.rstrip("\n")
            name, grade = line.split(":")
            if name not in grades:
                grades[name] = 0
            grades[name] += int(grade)
    for name in sorted(grades.keys(), key=lambda name: grades[name], reverse=True):
        print(f"{name:6}:{grades[name]:-3}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        exit(f"Usage: {sys.argv[0]} FILENAME")
    filename = sys.argv[1]
    add_grades(filename)

