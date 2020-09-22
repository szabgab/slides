seq = input('Type your DNA sequence here: ').upper()

codon_table = {
'Phe' : ['TTT', 'TTC'],
'Leu' : ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
'Ile' : ['ATT', 'ATC', 'ATA'],
'Met' : ['ATG'],
'Val' : ['GTT', 'GTC', 'GTA', 'GTG'],
'Ser' : ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
'Pro' : ['CCT', 'CCC', 'CCA', 'CCG'],
'Thr' : ['ACT', 'ACC', 'ACA', 'ACG'],
'Ala' : ['GCT', 'GCC', 'GCA', 'GCG'],
'Tyr' : ['TAT', 'TAC'],
'His' : ['CAT', 'CAC'],
'Gln' : ['CAA', 'CAG'],
'Asn' : ['AAT', 'AAC'],
'Lys' : ['AAA', 'AAG'],
'Asp' : ['GAT', 'GAC'],
'Glu' : ['GAA', 'GAG'],
'Cys' : ['TGT', 'TGC'],
'Trp' : ['TGG'],
'Arg' : ['CGT', 'CGC', 'GCA', 'CGG', 'AGA', 'AGG'],
'Gly' : ['GGT', 'GGC', 'GGA', 'GGG'],
'STOP' : ['TAA', 'TAG', 'TGA']
}

amino_acids = []
counter = {}
protein_sequence = []

while seq:
    amino_acids.append(seq[:3])
    seq = seq[3:]

for codon in amino_acids:
    if len(codon) < 3:
        print('The remaining bases: {} are not coding for an amino acid'.format(codon))
    for aa in codon_table:
        if codon in codon_table[aa]:
            if aa in counter:
                counter[aa] += 1
            else:
                counter[aa] = 1
            protein_sequence.append(aa)
            break

print(''.join(protein_sequence))

ordered = sorted(counter.keys())
for aa in ordered:
    print('{} {} - {:>5.2f} %'.format(aa, counter[aa], counter[aa]/len(protein_sequence)*100))
