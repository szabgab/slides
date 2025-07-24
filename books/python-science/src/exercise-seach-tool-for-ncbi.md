# Exercise: Search tool for NCBI


Write a program that can search NCBI and download and list sequences.

* `ncbi.py --term "SEARCH TERM" --download N` this will search the NCBI databasefor nucleotides using the the search term and download N results. It will also save the search term, the current date, the total number of items found, and the list of Ids downloaded in a JSON file along with the annotation from each ID".
* repeated use of the above command will save the new searches in the same JSON file.
* `ncbi.py --history` list all the previously executed search term along with the date it was used, the total number of items found and number of items downloaded. (This information is taken from the JSON file.)
* `ncbi.py --list` list some information about all the downloaded sequences. (e.g. the organism and taxonomy) along with the ID of each file.
* Optional: `ncbi.py --aa ID` print the distribution of Amino Acids in the sequences in the given ID"


