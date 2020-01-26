class Packets():
    def __init__(self, filename):
        self.filename = filename
        self.fh = open(filename)
        self.packets = {}
        self.max = {}

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            line = self.fh.readline()
            #print(f"line: {line}")
            if line == '':
                raise StopIteration

            line = line.rstrip("\n")
            if line == '':
                continue

            pid, seqid, maxseq, content = line.split(",")
            pid = int(pid)
            seqid = int(seqid)
            maxseq = int(maxseq)
            if pid not in self.packets:
                self.packets[pid] = {}
                self.max[pid] = maxseq
            if seqid in self.packets[pid]:
                raise Exception("pid arrived twice")
            if maxseq != self.max[pid]:
                raise Exception("maxseq changed")
            self.packets[pid][seqid] = content
            if len(self.packets[pid].keys()) == self.max[pid]:
                content = list(map(lambda i: self.packets[pid][i+1], range(self.max[pid])))
                del(self.max[pid])
                del(self.packets[pid])
                return content


