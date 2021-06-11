# Other
{id: other}

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

## Join file system path
{id: join-file-system-path}

* [Path](https://crystal-lang.org/api/Path.html)

![](examples/path.cr)


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

