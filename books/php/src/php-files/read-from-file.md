# Read from file


* fopen
* fgets

Use **fopen** with the parameter **r** to open a file for reading and then use **fgets** to read the content line-by-line.
Use **fclose** to close the filehandle.
PHP closes the file at the end of the program but it is better practice to close it by ourself.

{% embed include file="src/examples/files/readfile.php" %}


