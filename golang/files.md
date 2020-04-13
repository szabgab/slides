# Files
{id: files}

## Read file line-by-line with Scanner
{id: read-file-line-by-line-with-scanner}
{i: Open}
{i: os.Open}
{i: bufio}
{i: NewScanner}
{i: Scan}

![](examples/read-file-with-scanner/read_file_with_scanner.go)

## Read file line by line (os.Open)
{id: read-file-line-by-line}
{i: Open}
{i: NewReader}
{i: ReadString}
{i: readline}

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


## TODO: JSON
{id: json}

![](examples/json-round-trip/json_round_trip.go)


## TODO: Sum of numbers in a file
{id: sum-of-numbers}

![](examples/sum/sum.go)


