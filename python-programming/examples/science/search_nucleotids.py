from Bio import Entrez
Entrez.email = "gabor@szabgab.com"

term = "Cypripedioideae[Orgn] AND matK[Gene]"

handle = Entrez.esearch(db="nucleotide", term=term, idtype="acc")
record = Entrez.read(handle)
print(record["Count"])
# 519
print(record["IdList"])
# ['MK792700.1', 'MK792699.1', 'MK792698.1', ..., 'MK792681.1']


# term = "Orchid"
# 530077
# ['NZ_SELD00000000.2', 'NZ_SELD02000072.1',
