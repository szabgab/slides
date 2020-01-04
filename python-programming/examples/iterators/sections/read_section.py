import re

class SectionReader():
    def __init__(self, filename):
        self.filename = filename
        self.fh       = open(filename)

    def __iter__(self):
        return self

    def __next__(self):
        self.section = []
        while True:
            line = self.fh.readline()
            if not line:
                if self.section:
                    return self.section
                else:
                    self.fh.close()
                    raise StopIteration
            if re.search(r'\A\s*\Z', line):
                if self.section:
                    return self.section
                else:
                    continue
            self.section.append(line)


filename = 'planets.txt'
for sec in SectionReader(filename):
    print(sec)

