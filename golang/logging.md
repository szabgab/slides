# Logging
{id: logging}


## Simple Logging
{id: simple-logging}

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
![](examples/logging-to-file/log.log)

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


## TODO: log levels?
{id: logging-levels}

## TODO: log function names
{id: logging-function-names}

## TODO: logrotation
{id: logging-logrotation}
