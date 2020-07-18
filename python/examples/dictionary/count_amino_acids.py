dna = 'CACCCATGAGATGTCTTAACGCTGCTTTCATTATAGCCG'

aa_by_codon = {
    'ACG' : '?',
    'CAC' : 'Histidin',
    'CAU' : 'Histidin',
    'CCA' : 'Proline',
    'CCG' : 'Proline',
    'GAT' : '?',
    'GTC' : '?',
    'TGA' : '?',
    'TTA' : '?',
    'CTG' : '?',
    'CTT' : '?',
    'TCA' : '?',
    'TAG' : '?',
    #...
}

count = {}

for i in range(0, len(dna)-2, 3):
    codon = dna[i:i+3]
    #print(codon)
    aa = aa_by_codon[codon]
    if aa not in count:
        count[aa] = 0
    count[aa] += 1

for aa in sorted(count.keys()):
    print("{}  {}".format(aa, count[aa]))

