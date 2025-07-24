from Bio.Seq import Seq

# Nucleotide Sequences
my_dna = Seq("AGTACACTGGTAGGCCTTACAG_T")
print(my_dna)                       # AGTACACTGGTAGGCCTTACAG_T
print(my_dna.complement())          # TCATGTGACCATCCGGAATGTC_A
print(my_dna.reverse_complement())  # A_CTGTAAGGCCTACCAGTGTACT
print(my_dna.transcribe())          # AGUACACUGGUAGGCCUUACAG_U

my_rna = Seq("GAC_U")
print(my_rna)                       # GAC_U
print(my_rna.reverse_complement())  # A_GUC
print(my_rna.reverse_complement())  # A_GUC
print(my_rna.transcribe())          # GAC_U

