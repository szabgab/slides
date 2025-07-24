# Exercise: DNA sequencing

* Create a file called **dna_sequencing.py**
* A, C, T, G are called bases or nucleotides
* Accept a sequence on the command line like this:  **python dna_sequencing.py ACCGXXCXXGTTACTGGGCXTTGTXX**
* Given a sequence such as the one above (some nucleotides mixed up with other elements represented by an **X**)
* First return the sequences containing only ACTG. The above string can will be changed to **['ACCG', 'C', 'GTTACTGGGC', 'TTGT']**.
* Then sort them by lenght. Expected result: **['GTTACTGGGC', 'ACCG', 'TTGT', 'C']**

* Create a file called **extended_dna_sequencing.py**
* In this case the original string contains more than on type of foreign elements: e.g. **'ACCGXXTXXYYGTTQRACQQTGGGCXTTGTXX'**.
* Expected output: **['TGGGC', 'ACCG', 'TTGT', 'GTT', 'AC', 'T']**
* Ask for a sequence on the Standard Input (STDIN) like this:

```
python extended_dna_sequencing.py
Please type in a sequence:
```


