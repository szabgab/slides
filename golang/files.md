# Files
{id: files}

## Read file line-by-line with Scanner
{id: read-file-line-by-line-with-scanner}
{i: Open}
{i: os.Open}
{i: bufio}
{i: NewScanner}
{i: Scan}

* Removes the newlines

![](examples/read-file-with-scanner/read_file_with_scanner.go)

## Read file line by line with Reader
{id: read-file-line-by-line}
{i: Open}
{i: NewReader}
{i: ReadString}
{i: readline}

* Leaves the newlines at the end of the line

![](examples/read-file-line-by-line/read_file_line_by_line.go)

* [OS](https://golang.org/pkg/os/)


## Read file as one string (slurp)
{id: read-file-as-one-string}
{i: ReadFile}
{i: slurp}

![](examples/slurp-file/slurp_file.go)

## Write to file
{id: write-to-file}
{i: Create}
{i: WriteString}
{i: write}

![](examples/write/write_file.go)

## Write number to file
{id: write-number-to-file}

![](examples/write-number/write_number_file.go)

## Reading CSV file
{id: reading-csv-file}

![](examples/read-csv/process_csv_file.csv)

* Sum the numbers in the 3rd column

![](examples/read-csv/read_csv.go)


```
go run examples/read-csv/read_csv.go examples/csv/process_csv_file.csv
```

## Exercise: Sum of numbers in a file
{id: exercise-sum-of-numbers}

* Given a file where each row contains a number, print the sum of the numbers

![](examples/sum/sum.txt)

## Exercise: Count number of digitis
{id: exercise-count-number-of-digits}

Given a file like the following, write a program that will count how many times each digit appears:

![](examples/count-digits-in-file/numbers.txt)

## Exercise: ROT13 on file
{id: exercise-rot13-on-file}

* write a program that will accept the name of a file and replace it with the ROT13 encoded version of the text.
* Encode each letter a-z and A-Z, but leave everything else intact.
* If written correctly, running the program again on the same file should convert it back to the original version.

## Exercise: Selector with list of items from a file
{id: exercise-selector-with-list-of-items-from-a-file}

* Write a program that will get a file on the command line.
* It will display a menu allowing the user to select item by selecting the number next to it.
* e.g. the file looks like this:

```
blue
yellow
green
black
```

The menu should look like this:

```
1) blue
2) yellow
3) green
4) black
```

* The user then can select a number (e.g. 3) and the program prints "green".
* Make sure the program handles well if the input is invalid.


## TODO: Solution: Sum of numbers in a file
{id: solution-sum-of-numbers}

![](examples/sum/sum.go)


