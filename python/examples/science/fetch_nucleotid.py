from Bio import Entrez
Entrez.email = "gabor@szabgab.com"

#doc_id = 'MK792700.1'
doc_id = "EU490707"

# rettype="fasta"
handle = Entrez.efetch(db="nucleotide", id=doc_id, rettype="gb", retmode="text")
data = handle.read()
print(data)

