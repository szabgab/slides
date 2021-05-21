# Files
{id: files}

## Files intro
{id: files-intro}

* [File](https://crystal-lang.org/api/File.html)

## Read from file (slurp)
{id: read-from-file}
{i: read}
{i: slurp}

* Read the content of the whole file
* Raise exception `File::NotFoundError` if file does not exist

![](examples/files/read_from_file.cr)

## Read lines into array
{id: read-lines-into-array}
{id: read_lines}

![](examples/files/read_lines.cr)


## Read file line-by-line
{id: read-file-line-by-line}
{i: each_line}

![](examples/files/read_line_by_line.cr)

## Write to file
{id: write-to-file}
{i: write}

* Write the content to the file
* Raise exception if cannot open file for writing
* e.g. raise `File::NotFoundError` if parent directory does not exist

![](examples/files/write_to_file.cr)

## Append to file
{id: append-to-file}
{i: append}

![](examples/files/append_to_file.cr)


* This is a bug in my code, but it still creates the file with some strange rights `---xr-Sr--`

![](examples/files/append_to_file_bug.cr)

* The `ameba` linter will catch this error.

## Does file exist?
{id: file-exists}
{i: exists?}

![](examples/files/file_exists.cr)

## Size of file?
{id: size-of-file}
{i: empty?}
{i: size}

![](examples/files/file_size.cr)

## Last Modified date of file?
{id: modiffied-date-of-file}
{i: modification_time}

![](examples/files/modification_time.cr)

## Counter
{id: counter}

![](examples/files/counter.cr)

## Multi Counter JSON
{id: multi-counter-json}
{i: json}
{i: from_json}
{i: to_json}

![](examples/files/multi_counter_json.cr)


## Multi Counter YAML
{id: multi-counter-yaml}
{i: yaml}
{i: from_yaml}
{i: to_yaml}

![](examples/files/multi_counter_yaml.cr)
