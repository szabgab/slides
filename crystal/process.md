# Process
{id: process}

## Execute external program (system)
{id: execute-external-program-system}
{i: system}

![](examples/process/system.cr)

## Execute external program (backtick)
{id: execute-external-program-backtick}
{i: `}
{i: $?}
{i: success?}

* [command](https://crystal-lang.org/reference/syntax_and_semantics/literals/command.html)

![](examples/process/backtick.cr)

## Execute external program (Process)
{id: execute-external-program-process}
{i: exit}
{i: exit_code}
{i: exit_status}

* [Process](https://crystal-lang.org/api/Process.html)
* [Process::Status](https://crystal-lang.org/api/Process/Status.html)

![](examples/process/process.cr)

## Execute external program (capture)
{id: execute-external-program-capture}

![](examples/process/capture.cr)

## Execute external program (capture)
{id: execute-external-program-capture2}

![](examples/process/capture2.cr)

## Abort
{id: abort}
{i: abort}

{aside}
`abort` is the combination of printing to the `STDERR` and calling `exit` with an exit code.
{/aside}

![](examples/process/abort.cr)
![](examples/process/abort_code.cr)

* `abort` prints a message to STDERR and exit with exit code 1 (see `$?` or `%ERROR_LEVEL%`)
* Optionally we can supply the exit code as well.

