# Logging
{id: logging}


## Simple Logging
{id: simple-logging}

![](examples/logging/logger.go)

* There is a default prefix for each log message
* We can change this prefix using SetFlags
* By default log prints to STDERR (Standard Error)
* Fatal prints the message and exits the script with exit code 1

```
First
2019/10/08 23:47:13 First log
2019/10/08 23:47:13 0x490ef0
2019/10/08 23:47:13 logger.go:14: After setting flags
2019/10/08 23:47:13 logger.go:15: Oups
exit status 1
```

## Logging to a file
{id: logging-to-a-file}

* Set the output filehandle using `SetOutput`

![](examples/log-to-file/log2file.go)

* TODO: log levels?
* TODO: log function names

