# Exercise: Process N files in parallel

Create a script that given two number N and X will create N files (1.txt - N.txt). In each file put X rows of random ASCII characters: (digits, lower- and upper-case letters, space). (see [string](https://docs.python.org/library/string.html)) Each row should be 0-80 characters long. (random length for each row).
Using the script create a bunch of files.

Write a script that given a list of files will read all the files. For each file and count how many times each digit(!) appears and provide a combined report. First write the script in a single process (linear) way. Then convert it to be able to work with multiprocess. This version should also accept a number that indicates the size of the pool. Ideally you'd only need to write a few lines of code for this and you'd be able to use the code from the previous (linear) solution as a module

Submit the 3 scripts.

The report could look like this:

{% embed include file="src/examples/multiprocess/count_digits.out" %}

Create 100 files with 10000 rows in each one and measure how long the linear process takes vs the parallel process with various numbers.



