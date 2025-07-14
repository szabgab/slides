# Exercise: DNA Sequence Analyzer with callback


The above can work, but if the file is huge, we might not be able to hold all the list in memory.
Change the read_file function that to allow the user to supply the analyze function
(or rather the reference to the analyze function) as a parameter. See the skeleton below.
The output should be the same as above.


{% embed include file="src/examples/references/dna2_skeleton.pl" %}


