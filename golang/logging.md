# Logging
{id: logging}


## Simple Logging
{id: simple-logging}

* [log](https://golang.org/pkg/log/)

![](examples/logging/logger.go)
![](examples/logging/logger.out)

* By default log prints to STDERR (Standard Error)

* There is a default prefix for each log message
* We can change this prefix using SetFlags

## Logging Fatal errors
{id: logging-fatal-errors}

* `Fatal`, `Fatalf`, and `Fataln` print the message and call `os.Exit(1)` for the program to  exit with code 1.
* Does not execute the lines after calling `Fatal`

![](examples/logging-fatal/logging_fatal.go)
![](examples/logging-fatal/logging_fatal.out)


## Logging to a file - rewrite
{id: logging-to-a-file}

* Set the output filehandle using `SetOutput`

![](examples/logging-to-file/logging_to_file.go)
![](examples/logging-to-file/logging_to_file.log)

## Logging to a file - append
{id: append-to-logfile}

![](examples/logging-to-file-append/logging_to_file_append.go)
![](examples/logging-to-file-append/log.log)


## Logging flags
{id: logging-flags}

![](examples/logging-flags/logging_flags.go)


## Logging the ilename
{id: logging-the-filename}


![](examples/logging-filename/logging_filename.go)
![](examples/logging-filename/logging_filename.out)


## Logging: Set Prefix
{id: logging-set-prefix}
{i: SetPrefix}
{i: Prefix}

* `SetPrefix` can set the prefix
* `Prefix` returns the current prefix

![](examples/logging-set-prefix/logging_set_prefix.go)
![](examples/logging-set-prefix/logging_set_prefix.out)

## Turn logging on/off
{id: logging-turn-on-off}
{i: Output}
{i: Discard}
{i: NullWriter}
{i: /dev/null}
{i: Stderr}

{aside}
By default the log module writes to the standard error (STDERR). We can turn off the logging by setting the `Output` channel to `ioutil.Discard`.
We can turn on the logging again by setting the `Output` channel to `os.Stderr`. 
{/aside}

![](examples/logging-off/logging_off.go)
![](examples/logging-off/logging_off.out)


## TODO: log levels?
{id: logging-levels}

## TODO: log function names
{id: logging-function-names}

## TODO: logrotation
{id: logging-logrotation}
