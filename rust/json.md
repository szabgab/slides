# JSON
{id: json}

## JSON serialize examples
{id: json-serialize-examples}
{i: json}

![](examples/json/json-serialize/Cargo.toml)
![](examples/json/json-serialize/src/main.rs)

## JSON serialize struct
{id: json-serialize-struct}

![](examples/json/json-serialize-struct/Cargo.toml)
![](examples/json/json-serialize-struct/src/main.rs)

## serde
{id: serde}
{i: Serialize}
{i: Deserialize}
{i: to_string}
{i: from_string}

![](examples/json/serde-demo/Cargo.toml)
![](examples/json/serde-demo/src/main.rs)

## serde manipulate json (change, add)
{id: serde-manipulate-json}
{i: json}
{i: get_mut}

![](examples/json/serde-manipulate-json/Cargo.toml)
![](examples/json/serde-manipulate-json/src/main.rs)


## JSON serialize struct with date
{id: json-serialize-struct-with-date}

![](examples/json/json-serialize-struct-with-date/Cargo.toml)
![](examples/json/json-serialize-struct-with-date/src/main.rs)

* Deserialize into struct
* Read multi-json files (the result of a json-based logger)

## Read JSON file
{id: read-json-file}
{i: serde_json}
{i: from_str}
{i: Value}

* We would like to read the following simple JSON file:

![](examples/json/json-read-from-file/data.json)

* We need [serde](https://serde.rs/) and [serde_json](https://docs.rs/serde_json/latest/serde_json/)

![](examples/json/json-read-from-file/Cargo.toml)

* We first open the file and read the content of the file.
* Then we parse the string in two ways.
* Once into a generic `serde::Value` structure. In this case we need to extract and convert the values.
* Once into a pre-defined `struct`.

* TODO: show in both cases how to handle cases when a fiedl is missing or the value is incorrect type (eg. we have  "x": "qqrq")
* TODO: show in both cases what happens if there are fields in the JSON file that we don't know about in the struct.
* TODO: show lists in the JSON file
* TODO: show deeper structure


![](examples/json/json-read-from-file/src/main.rs)

![](examples/json/json-read-from-file/out.out)


## Read JSON file using from_reader
{id: read-json-file-using-from-reader}
{i: from_reader}

![](examples/json/json-read-from-reader/data.json)

![](examples/json/json-read-from-reader/Cargo.toml)

![](examples/json/json-read-from-reader/src/main.rs)

![](examples/json/json-read-from-reader/out.out)
