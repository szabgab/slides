# Python and Biology
{id: biology}

## Biopython
{id: bio-python}

* [Biopython](http://biopython.org/)
* [Biopython GitHub project](https://github.com/biopython/biopython)
* [Biopython Tutorial and Cookbook](http://biopython.org/DIST/docs/tutorial/Tutorial.html)


## Biopython background
{id: bio-python-background}

* [Sequence formats](https://www.genomatix.de/online_help/help/sequence_formats.html) (FASTA, FASTQ, EMBL, ...)
* [FASTA](https://en.wikipedia.org/wiki/FASTA_format)
* [FASTQ](https://en.wikipedia.org/wiki/FASTQ_format)
* [EMBL](https://en.wikipedia.org/wiki/European_Molecular_Biology_Laboratory) European Molecular Biology Laboratory
* [Gene names symbols](https://ghr.nlm.nih.gov/about/gene-names-symbols)


## Bio python sequences
{id: bio-python-sequences}

![](examples/science/sequences.py)

![](examples/science/sequences_err.py)

## Download and Read FASTA, GenBank files
{id: bio-python-read-fasta-files}

For example the data about Orchids in two formats:

* [ls_orchid.fasta](https://raw.githubusercontent.com/biopython/biopython/master/Doc/examples/ls_orchid.fasta) in FASTA format
* [ls_orchid.gbk](https://raw.githubusercontent.com/biopython/biopython/master/Doc/examples/ls_orchid.gbk) in GenBank format

Download those files and use them:

![](examples/science/read_fasta.py)

## Search NCBI and Download FASTA and GenBank files
{id: bio-python-download-data}

Use the NCBI (National Center for Biotechnology Information) database to search  manually for [nucleotide](https://www.ncbi.nlm.nih.gov/nucleotide)
or tons of other types of data. Then one can download the files manually from the web site.


## Search nucleotids
{id: bio-python-search-nucleotids}

You can also search the same database programmatically.

![](examples/science/search_nucleotids.py)


## Download nucleotids
{id: bio-python-download-nucleotids}

![](examples/science/fetch_nucleotid.py)


## Exercise: Nucleotid
{id: exercise-bio-python-nucleotid}

* Search for your favorite nucleotid
* Print out the number of results
* Download the 3 different sequences from the list (using the id) in GeneBank format and save them in files using the id as the name of the file and .gb as the extension
* Write a separate script that reads and displays the sequences.

## Exercise: Search tool for NCBI
{id: exercise-seach-tool-for-ncbi}

Write a program that can search NCBI and download and list sequences.

* `ncbi.py --download --term "SEARCH TERM" --download N` this will search the NCBI databasefor nucleotides using the the search term and download N results. It will also save the search term, the current date, the total number of items found, and the list of Ids downloaded in a JSON file along with the annotation from each ID".
* repeated use of the above command will save the new searches in the same JSON file.
* `ncbi.py --history` list all the previously executed search term along with the date it was used, the total number of items found and number of items downloaded. (This information is taken from the JSON file.)
* `ncbi.py --list` list some information about all the downloaded sequences. (e.g. the organism and taxonomy) along with the ID of each file.
* Optional: `ncbi.py --aa ID` print the distribution of Amino Acids in the sequences in the given ID"




## Biology background
{id: biology-background}

* [Genetics - inheritance](https://www.nhs.uk/conditions/genetics/inheritance/)
* [Genetic inheritance](https://basicbiology.net/micro/genetics/genetic-inheritance)
* [What's a genome Chp2 1](http://www.genomenewsnetwork.org/resources/whats_a_genome/Chp2_1.shtml)
* [What's a genome Chp4 1](http://www.genomenewsnetwork.org/resources/whats_a_genome/Chp4_1.shtml)
* alleles, genotype, phenotype


