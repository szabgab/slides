# Introduction to Perl
{id: introduction-to-perl}

## First script
{id: first-perl-script}

![](examples/hello_world.pl)

* #!/usr/bin/env perl  - Path to perl interpreter
* use v5.10;           - Minimal version number of Perl, turn on new features.
* use strict;          - Require variable declarations, avoid stupid mistakes.
* use warnigs;         - Ask for warnings. Avoid further stupid mistakes. 

* say                  - print with newline at the end

## print vs. say
{id: print-vs-say}

* say   - (since perl 5.10) newline at the end
* print - (always)
* print "...\n";    - add the newline

## Scalar values
{id: scalar-values}

"A string"

'Another string'

23

23.45

## Lists
{id: perl-lists}

('string', 42, 2.3)

## Hash
{id: perl-hash}

(
    'name'  => 'Foo Bar',
    'email' => 'foo@bar.com',
) 


## Functions
{id: perl-functions}

sub greeting {
    say 'Hello World';
}


## Variable declaration
{id: variable-declaration}

my $name;
$name = 'Foo Bar';

my $email = 'foo@bar.com';

## Sigils
{id: sigils}

* $ - scalars
* @ - arrays
* % - hashes
* & - functions

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
open my $fh, '<', $filename or die "Could not open '$filename' for reading";

open my $fh, '>', $filename or die "Could not open '$filename' for writing";

open my $fh, '>>', $filename or die "Could not open '$filename' to append";
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

* File::Basename
* Cwd 

## Selected Perl modules
{id: selected-perl-modules}

* DBI for database access
* DBD:: database drivers
* XML
* Config file (INI)
* CSV
* YAML
* JSON

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


