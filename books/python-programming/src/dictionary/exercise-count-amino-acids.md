# Exercise: Count Amino Acids

* Each sequence consists of many repetition of the 4 bases represented by the ACTG characters.
* There are 64 codons (sets of 3 bases following each other)
* There are 20 [Amino Acids](https://en.wikipedia.org/wiki/Amino_acid) each of them are represented by 3 bases (by one codon).
* Some of the Amino Acids can be represented in multiple ways, represented in the [Codon Table](https://en.wikipedia.org/wiki/DNA_codon_table). For example Histidine can be encoded by both CAU, CAC

* Create a file called **count_amino_acids.py** that given a file witha  DNA sequence in it, will count the Amino acids from the sequence.
* Read the sequence saved in a txt file.
* You can generate a sequence with a random number generator and save it to that file, but it would be much better if you used a real sequence.
* An even better way would be to read the sequence from a FASTA file. You can download one from [NCBI](https://www.ncbi.nlm.nih.gov/).

* Skeleton:

{% embed include file="src/examples/dictionary/count_amino_acids_skeleton.py" %}

* You will want to convert this to a dictionary that maps each codon to an Amino Acid. Do it programmatically!



