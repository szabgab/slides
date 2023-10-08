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

![](examples/csv/csv-stringrecord/planets.csv)
![](examples/csv/csv-stringrecord/Cargo.toml)
![](examples/csv/csv-stringrecord/src/main.rs)
![](examples/csv/csv-stringrecord/out.txt)

## Read CSV file into hashes
{id: read-csv-file-into-hashes}
{i: csv}
{i: HashMap}

![](examples/csv/csv-hash/planets.csv)
![](examples/csv/csv-hash/Cargo.toml)
![](examples/csv/csv-hash/src/main.rs)
![](examples/csv/csv-hash/out.txt)

## Read CSV file as structs
{id: read-csv-file-into-structs}
{i: csv}
{i: struct}

![](examples/csv/csv-struct/planets.csv)

![](examples/csv/csv-struct/Cargo.toml)
![](examples/csv/csv-struct/src/main.rs)

![](examples/csv/csv-struct/out.txt)

## Read CSV to struct, add extra fields
{id: read-csv-to-struct-with-extra-fields}

![](examples/csv/csv-struct-extra-fields/Cargo.toml)
![](examples/csv/csv-struct-extra-fields/out.txt)
![](examples/csv/csv-struct-extra-fields/planets.csv)
![](examples/csv/csv-struct-extra-fields/src/main.rs)

## CSV TODO
{id: csv-todo}

* What if a field is missing (basically there is an empty string instead of the value) How can we set a default value for that? Especially numerical columns.
* What if a field has "na" in it meaning not available? Especially numerical columns.
* How can we skip a row (e.g. if one of the fields is missing)?

