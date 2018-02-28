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

## print vs. say
{id: print-vs-say}

* say   - (since perl 5.10) newline at the end
* print - print as it is
* print "...\n";    - add the newline

## Scalar values - strings
{id: scalar-values-strings}

"A string"

'Another string'

## Scalar values - numbers
{id: scalar-values-numbers}

for numbers there is no need for quotes

integer

```
26
1_234_567                # like 1,234,567 in human writing
```

integer (hex/oct/binary)

```
0x1a            # hex     also written as    hex("1a");
032             # oct     also written as    oct("32");
0b11010         # binary  also written as    oct("0b11010");
                # all 3 equal to 26 decimal
```

real or floating-point

```
3.5e+3          # 3500
```

## Lists
{id: perl-lists}

('string', 42, 2.3)

## Hash
{id: perl-hash}

```
(
    'name'  => 'Foo Bar',
    'email' => 'foo@bar.com',
)
```

```
(
    'banane' => 7,
    'apple' => 3,
    'lemon' => 1,
)
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

my @names = ('Foo', 'Bar', 'Moo');
say $names[0];

scalar @names;      # number of elements in the array
$#names;            # the largest index (one less than number of elements)

push @names, 'Minimacko';
pop @names;
shift @names;
unshift @names, 'Malacka';

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

## Loops (for, foreach, while)
{id: loops}

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

