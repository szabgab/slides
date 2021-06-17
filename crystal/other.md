# Other
{id: other}

## Spaceship Operator
{id: spaceship-operator}
{i: <=>}

![](examples/spaceship_operator.cr)

## Check if variable is nil?
{id: nil}
{i: nil}
{i: nil?}

![](examples/is_nil.cr)

## Single quotes vs double quotes
{id: single-quotes-vs-double-quotes}

* Single quotes are for characters
* Double quotes are for strings


## No type-checking?
{id: no-typechecking}

![](examples/assign_to_variable.cr)
![](examples/assign_to_variable.out)

## HTTP Client
{id: http-client}
{i: http/client}
{i: HTTP::Client}

![](examples/http_client.cr)


## Divide by zero is Infinity
{id: divide-by-zero-is-infinity}
{i: Infinity}

![](examples/divide_by_zero.cr)

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

## Execute external program (capture)
{id: execute-external-program-capture2}

![](examples/capture2.cr)


## Ameba Linter
{id: ameba-linter}


* [Ameba](https://github.com/crystal-ameba/ameba)

![](.ameba.yml)

```
shards install
./bin/ameba
```

## Parse URL (URI)
{id: parse-url}
{i: URI}

![](examples/parse_url.cr)

## Join / concatenate file system path
{id: join-file-system-path}
{i: Path}

* [Path](https://crystal-lang.org/api/Path.html)

![](examples/path.cr)

## Join / concatenate file system path
{id: concatenate-file-system-path}
{i: Path}
{i: /}

![](examples/concatenate_path.cr)

## Path from string
{id: path}

![](examples/path_from_string.cr)


## Expand Path
{id: expand-path}
{i: expand}
{i: ~}

![](examples/path_expand.cr)
![](examples/path_expand.out)


## Ternary operator and or to set default value
{id: default-value}
{i:||}
{i: ?:}

![](examples/default.cr)

## Gravatar
{id: gravatar}
{i: Digest::MD5.hexdigest}

![](examples/gravatar.cr)

## Try Crystal
{id: try}

![](examples/try.cr)

## case / when
{id: case}
{i: case}
{i: switch}
{i: when}

![](examples/case.cr)

## STDERR, STDOUT
{id: stderr}
{i: STDERR}
{i: STDOUT}

![](examples/stderr.cr)

* Redirection on the command line using > out  and 2> err

## Suffix if
{id: suffix-if}
{i: if}

![](examples/suffix_if.cr)

## Suffix unless
{id: suffix-unless}
{i: unless}

![](examples/suffix_unless.cr)

## Return Boolean
{id: return-boolean}

![](examples/functions/return_bool.cr)

## Symbols
{id: symbols}

![](examples/symbols.cr)

## Macros
{id: macros}

![](examples/macros/function.cr)

