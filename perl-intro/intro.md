# Introduction to Perl
{id: introduction-to-perl}

## Overview
{id: overview}

Basics of the language:

* Scalars, arrays, hashes
* Function definition
* Regexes
* Control structures (if, else, for, while)
* IO (screen, keyboard, files)
* References
* Introduce multi dimensional data structures
* Packages
* OOP
* Anonymous functions, dispatch tables
* Introduce CPAN (MetaCPAN)
* Go over a number of modules for text processing

## First script
{id: first-perl-script}

![](examples/hello_world.pl)

* #!/usr/bin/env perl  - Path to perl interpreter
* use v5.10;           - Minimal version number of Perl, turn on new features.
* use strict;          - Require variable declarations, avoid stupid mistakes.
* use warnigs;         - Ask for warnings. Avoid further stupid mistakes.

* say                  - print with newline at the end

## Always use strict and use warnings!
{id: always-use-strict-and-use-warnings}

* [Always use strict and use warnings in your perl code!](https://perlmaven.com/always-use-strict-and-use-warnings)
* [Always use warnings in your Perl code!](https://perlmaven.com/always-use-warnings)

## Avoid global variables
{id: avoid-global-variables}

* Not really Perl specific, but make variables as tight as possible!
* You will thank yourself a year later.

## Keep it simple
{id: keep-it-simple}

* A script has to be simple, readable and reusable.
* Sophisticated optimization and algorithms are less interesting.

## First script with main function
{id: first-perl-scirpt-with-main}

![](examples/hello_world_main.pl)

* Putting all your code in small(!) functions will make your code better.

## Comments
{id: comments-in-perl}

Anywhere (except th first row) a `#` starts a comment till the end of the row.

```
# Comment
say "somthing"; # comment
```

## print vs. say
{id: print-vs-say}

* say  "hello";    # print a newline at the end. (available since perl 5.10)
* print "hello";   # print as it is
* print "hello\n"; # print a newline at the end.

## Scalar values
{id: scalar-values}

* `undef`
* a number
* a string
* a reference to any other data structure or function

## Scalar values - undef
{id: scalar-values-undef}

`undef` corresponds to `NULL` in SQL, `None` in Python, and `null` in PHP or JavaScript.

## Scalar values - strings
{id: scalar-values-strings}

A string can be either double quoted or single quoted. Differences explained later.

```
"A string"

'Another string'
```

## Scalar values - numbers
{id: scalar-values-numbers}

For numbers there is no need for quotes.

*integer*

```
26
1_234_567                # like 1,234,567 in human writing
```

*integer (hex/oct/binary)*

```
0x1a            # hex     also written as    hex("1a");
032             # oct     also written as    oct("32");
0b11010         # binary  also written as    oct("0b11010");
                # all 3 equal to 26 decimal
```

*real or floating-point*

```
3.5e+3          # 3500
```

## Lists
{id: perl-lists}

A list is a series of scalar values separated by comma and enclosed in parentheses.
The scalar values themselves can be references to other data structures.
(An array, explained later is a variable holding a list.)

```
('string', 42, 2.3)
```

## Hash
{id: perl-hash}

A hash is a set of key-value pairs. The keys are strings that are unique in the given hash.
The values are scalars, including references to other data structures.
In PHP they are calle "associative arrays". In Python "dictionaries".

```
(
    'name'  => 'Foo Bar',
    'email' => 'foo@bar.com',
)
```

```
(
    'banana' => 7,
    'apple' => 3,
    'lemon' => 1,
)
```

## Boolean values
{id: boolean-values}

In Perl there is no special True and False values. Any value can be checked for True-ness. The following values are considered to be false:

* `undef`
* 0        # the number 0.
* ''       # empty string.
* '0'      # a string with a single 0 in it.

## String Operators
{id: string-operators}

```
"abc" . "def"     # concatenation
"abc" x 3         # repetition operator
```

## Numerical Opertors
{id: numerical-operators}

```
2 + 3        # 5
2 * 3        # 6
2 ** 3       # 2*2*2 = 8
....
```

## Perl is an Operator driven language
{id: operator-driven-language}

```
"2" . "3"     # "23"
"2" . 3       # "23"
2   . 3       # "23"

"2" + "3"     # 5
"2" + 3       # 5
```

```
"abc" . "def"    # "abcdef"
"abc" + "def"    # 0  + 2 warnings about Argument isn't numeric in addition (+)
```

## Variables
{id: variables}

Sigil + variable name:

```
$name_of_a_scalar
@name_of_an_array
%name_of_a_hash
```

Variables (and other names) are case sensitive

```
$h
$H
```

## Sigils
{id: sigils}

* $ - scalars
* @ - arrays
* % - hashes
* & - functions

## Variable declaration
{id: variable-declaration}

my $name;
$name = 'Foo Bar';

my $email = 'foo@bar.com';

## Arrays
{id: arrays}

```
my @people;                           # Declare empty array.
my @names = (                         # Declare array and assign 3 elements.
    'Foo',
    'Bar',
    'Moo',                            # Trailing comma is ok.
);
say $names[0];                        # Access the 0th element 'Foo'
```
```
scalar @names;      # number of elements in the array
$#names;            # the largest index (one less than number of elements)
```

```
push @names, 'Minimacko';
pop @names;
shift @names;
unshift @names, 'Malacka';
```

## Hashes
{id: hashes}

my %phone = (
    'Foo' => '01-23456',
    'Bar' => '98-76543',
);
say $phone{'Foo'};
$phone{'Zorg'} = '999'

for (my $name keys %phone) {
    say "$name $phone{$name}";
}


## IO (screen, keyboard)
{id: io}

## IO (files)
{id: io-files}

```
open my $fh, '<', $filename or die "Could not open '$filename' for reading $!";

open my $fh, '>', $filename or die "Could not open '$filename' for writing $!";

open my $fh, '>>', $filename or die "Could not open '$filename' to append $!";
```

## Control structures (if, else, elsif)
{id: control-structures}

## For Loops (for, foreach)
{id: for-loops}

## While Loops
{id: while-loops}


## Loop controls (next, last, redo)
{id: loop-controls}

* next - evaluate the loop condition and if it is true go to the next iteration
* last - exit the loop
* redo - start the iteration again without evaluating the loop condition

## C-style for loop
{id: c-style-for-loop}

Possible, but not recommended in Perl.

## References
{id: references}

```
my @names = ('foo', 'bar', 'baz')
my $ref_to_names = \@names;

@names          @$ref_to_names
$name[0]        $$ref_to_names[0]  better yet write   $ref_to_names->[0]

sacalar @names      scalar @$ref_to_names

```

## Functions
{id: perl-functions}

sub greeting {
    say 'Hello World';
}

## Anonymous functions (state machine as an example), dispatch tables
{id: anonymous-functions}

## Dispatch table
{id: dispatch-table}



## Linux environment variables (%ENV)
{id: linux-environment-variables}

![](examples/env.pl)

## List all defined variables
{id: list-all-defined-variables}

![](examples/list_defined_variables.pl)

## Regexes
{id: regexes}

* [Perl 5 Regex cheat sheet](https://perlmaven.com/regex-cheat-sheet)

## Packages
{id: packages}

## OOP
{id: oop}

* Perl core
* Moo
* Moose
* ...

## OOP Perl core
{id: oop-perl-core}

![](examples/MyClass.pm)


## Perl internal variables
{id: perl-internal-variables}

* $! - error of the last system call e.g. [open file](https://perlmaven.com/beginner-perl-maven-no-such-file)
* $/ - input record separator, [slurp mode](https://perlmaven.com/slurp)
* $_ - the [default variable](https://perlmaven.com/the-default-variable-of-perl) for many operations
* $0 - Name of the current program
* $1, $2, .. Regex match variables
* @ARGV - command line parameters
* @_ - parameters of the current function

Full list at [perldoc perlvar](https://metacpan.org/pod/distribution/perl/pod/perlvar.pod)

## CPAN
{id: cpan}

* [CPAN](https://www.cpan.org/)
* [sco](http://search.cpan.org/) old, but well indexed by Google
* [Meta::CPAN](https://metacpan.org/) new, maintaned, open source
* mcpan - search.mcpan.org

## Install CPAN Modules
{id: install-cpan-modules}

* Use the packaging system of your OS
* `cpan`
* `cpanm` from [cpanmin.us](https://cpanmin.us/)
* Ask your sysadmin

## Selected Standard Perl Modules
{id: selected-stadard-perl-modules}

* Data::Dumper
* File::Basename
* Cwd

## Selected Perl modules
{id: selected-perl-modules}

* Datetime (date manipulation)
* Datetime::Tiny
* DBI for database access
* DBD:: database drivers
* XML
* Config file (INI)
* CSV
* YAML
* JSON
* Logging

## Database access
{id: database-access}

* [DBI](https://metacpan.org/pod/DBI)
* [DBD::SQLite](https://metacpan.org/pod/DBD::SQLite)
* [DBD::mysql](https://metacpan.org/pod/DBD::mysql)
* [DBD::Oracle](https://metacpan.org/pod/DBD::Oracle)
* [DBD::Pg](https://metacpan.org/pod/DBD::Pg)

## YAML
{id: yaml}

* [YAML on Perl Maven](https://perlmaven.com/yaml)

## JSON
{id: json}

* [JSON on Perl Maven](https://perlmaven.com/json)

## Config INI files
{id: config-ini-files}

* [Config::Tiny on Perl Maven](https://perlmaven.com/pro/reading-configuration-files-in-perl)

## CSV
{id: csv}

* [CSV on Perl Mave](https://perlmaven.com/csv)
* [Text::CSV](https://metacpan.org/pod/Text::CSV)
* [Text::CSV_XS](https://metacpan.org/pod/Text::CSV)

## Logging
{id: logging}

* [Log4perl the easy way](https://perlmaven.com/logging-in-modules-with-log4perl-the-easy-way)

## Perl::Critic - lint for Perl
{id: perl-critic}

* [Perl::Critic](https://perlmaven.com/perl-critic)

## Perl Resources
{id: perl-resources}

* [MetaCPAN](https://metacpan.org/)
* [Perlmonks](http://www.perlmonks.org/)
* [Perl Maven](https://perlmaven.com/)
* [Perl Weekly](http://perlweekly.com/)
* [Stack Overflow Perl](https://stackoverflow.com/questions/tagged/perl)

