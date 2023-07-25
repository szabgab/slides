# CSV
{id: csv}

## Read CSV file as a vector of StringRecords
{id: read-csv-file-as-a-vector-of-stringrecords}
{i: csv}
{i: StringRecord}

* [csv](https://crates.io/crates/csv)
* [StringRecord](https://docs.rs/csv/latest/csv/struct.StringRecord.html)

* We read the rows (skipping the first row)
* We can iterate over the rows or access the individual elements

![](examples/csv-stringrecord/planets.csv)
![](examples/csv-stringrecord/Cargo.toml)
![](examples/csv-stringrecord/src/main.rs)
![](examples/csv-stringrecord/out.txt)

## Read CSV file into hashes
{id: read-csv-file-into-hashes}
{i: csv}
{i: HashMap}

![](examples/csv-hash/planets.csv)
![](examples/csv-hash/Cargo.toml)
![](examples/csv-hash/src/main.rs)
![](examples/csv-hash/out.txt)

## Read CSV file as structs
{id: read-csv-file-into-structs}
{i: csv}
{i: struct}

![](examples/csv-struct/planets.csv)

![](examples/csv-struct/Cargo.toml)
![](examples/csv-struct/src/main.rs)

![](examples/csv-struct/out.txt)
