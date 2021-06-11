# CLI
{id: cli}

## ARGV
{id: argv}
{i: ARGV}

* The raw values from the command line can be found in the `ARGV` array.

![](examples/cli/argv.cr)

## Usage statement and exit
{id: usage-statement-and-exit}

![](examples/cli/some_program.cr)

## Command line Option Parser (argparse, GetOpts)
{id: option-parser}

* [OptionParser](https://crystal-lang.org/api/OptionParser.html)

![](examples/cli/cli_parser.cr)

* `cli_parser.cr -d code-maven.com -v`
* `cli_parser.cr -d`
* `cli_parser.cr -x`

## Pass parameters to OptionParser
{id: parameters-for-option-parser}

![](examples/cli/parse_options.cr)
![](examples/cli/parse_options.out)

## Order of parsing

![](examples/cli/parsing_order.cr)
![](examples/cli/parsing_order.out)

