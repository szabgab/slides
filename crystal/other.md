# Other
{id: other}

## Single quotes vs double quotes 
{id: single-quotes-vs-double-quotes}

* Single quotes are for characters
* Double quotes are for strings


## No type-checking?
{id: no-typechecking}

```
x = "one"
x = 1
p! x
p! typeof(x)
```

## JSON (to_json, parse)
{id: json}
{i: json}
{i: to_json}
{i: parse}

* Round trip with JSON
* Have to `require "json"` for the method to be added.

![](examples/json.cr)

## HTTP Client
{id: http-client}

![](examples/http_client.cr)


## Divide by zero is Infinity
{id: divide-by-zero-is-infinity}
{i: Infinity}

![](examples/divide_by_zero.cr)

## Catch exception - begin, rescue
{id: catch-exception}
{i: begin}
{i: rescue}

![](examples/catch_exception.cr)

## Raise exception
{id: raise-exception}

![](examples/raise_exception.cr)

## Require other files
{id: require-other-files}

* [requiring files](https://crystal-lang.org/reference/syntax_and_semantics/requiring_files.html)

![](examples/one/welcome.cr)
![](examples/one/use_welcome.cr)

## List Methods
{id: list-methods}

![](examples/methods.cr)
![](examples/methods.out)


## Checking the slides
{id: checking-the-slides}

![](examples/check_slides.cr)

## Crystal mine
{id: crystal-mine}

![](examples/mine.cr)

## Execute external program (system)
{id: execute-external-program-system}
{i: system}

![](examples/system.cr)

## Execute external program (backtick)
{id: execute-external-program-backtick}
{i: `}
{i: $?}
{i: success?}

* [command](https://crystal-lang.org/reference/syntax_and_semantics/literals/command.html)

![](examples/backtick.cr)

## Execute external program (Process)
{id: execute-external-program-process}
{i: exit}
{i: exit_code}
{i: exit_status}

* [Process](https://crystal-lang.org/api/Process.html)
* [Process::Status](https://crystal-lang.org/api/Process/Status.html)

![](examples/process.cr)

## Execute external program (capture)
{id: execute-external-program-capture}

![](examples/capture.cr)


## Ameba Linter
{id: ameba-linter}


* [Ameba](https://github.com/crystal-ameba/ameba)

![](.ameba.yml)

```
shards install
./bin/ameba
```

## Crystal logging
{id: crystal-logging}

* [Log](https://crystal-lang.org/api/Log.html)

* 7 levels of logging, default is `info` and higher to the `STDOUT`

![](examples/logging.cr)

## Parse URL (URI)
{id: parse-url}
{i: URI}

![](examples/parse_url.cr)

## Join file system path
{id: join-file-system-path}

* [Path](https://crystal-lang.org/api/Path.html)

![](examples/path.cr)


## Command line Option Parser (argparse, GetOpts)
{id: option-parser}

* [OptionParser](https://crystal-lang.org/api/OptionParser.html)

![](examples/cli_parser.cr)

* `cli_parser.cr -d code-maven.com -v`
* `cli_parser.cr -d`
* `cli_parser.cr -x`

## YAML
{id: yaml}
{i: YAML}

* [YAML](https://crystal-lang.org/api/YAML.html)

![](examples/crystal.yml)
![](examples/use_yaml.cr)

## SQLite
{id: sqlite}
{i: SQLite}

![](examples/try_sqlite.cr)

## Multi-counter with SQLite
{id: multi-counter-sqlite}
{i: SQLite}

![](examples/multi_counter_sqlite.cr)