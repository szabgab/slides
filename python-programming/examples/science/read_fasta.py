from Bio import SeqIO
import requests

def get_file(url, filename):
    res = requests.get(url)
    if res.status_code != 200:
        raise Exception("Could not get file")

    with open(filename, 'w') as fh:
        fh.write(res.text)


def process_file(filename, file_type):
    for seq_record in SeqIO.parse(filename, file_type):
        print(seq_record.id)
        print(repr(seq_record.seq))
        print(len(seq_record))


fasta_url = 'https://raw.githubusercontent.com/biopython/biopython/master/Doc/examples/ls_orchid.fasta'
filename = "ls_orchid.fasta"
file_type = "fasta"
get_file(fasta_url, filename)
process_file(filename, file_type)


genbank_url = "https://raw.githubusercontent.com/biopython/biopython/master/Doc/examples/ls_orchid.gbk"
filename = "ls_orchid.gbk"
file_type = "genbank"
get_file(genbank_url, filename)
process_file(filename, file_type)
