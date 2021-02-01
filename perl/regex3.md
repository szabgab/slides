# Regular Expressions
{id: regex3}


## Regexp::Common
{id: regexp-common}

![](examples/regex-perl/regexp_common.pl)
![](examples/regex-perl/regexp_common.txt)


## Options and modifiers
{id: regex-options-modifiers}

```
//    is actually the same as    m//
When using the m sign you can change the delimiters:
Let's say you would like to match lines with

/usr/bin/perl
```

```
if ($line =~ /\/usr\/bin\/test-perl/) {
}

if ($line =~ m{/usr/bin/perl}) {
}
```


## /i  Case sensitivity
{id: regex-case-sensitivity}

```
$line = "Apple";
/apple/      # does not match
/apple/i     # case insensitive will match
```


## Matching quotes
{id: matching-quotes}

![](examples/regex-perl/sentences.txt)
![](examples/regex-perl/matching_quotes.pl)


## /s single line
{id: regex-s-modifier}

```
. will match any character (including newline)
```


## /m multiple lines
{id: regex-m-modifier-multiple-lines}

```
^ will match beginning of line
$ will match end of line

\A still matches beginning of string
\z
\Z
```
![](examples/regex-perl/find_letter_change.pl)



## /x enable white spaces and comments
{id: regex-x-modifier}

```
/(X\d+).*\1/

/
 (X\d+)         # product number
 .*             # any character
 \1             # the same product number
/x
```


## Substitute
{id: substitute}

* s/PATTERN/REPLACEMENT/
* s{PATTERN}{REPLACEMENT}


```
$line = "abc123def";

$line =~ s/\d+/ /;       # "abc def"


$line =~ s{
      ([a-z]*)
      (\d*)
      ([a-z]*)
      }
      {$3$2$1}x;        # "def123abc"

```


## Global substitute
{id: global-substitute}

```
$line = "abc123def";

$line =~ s/.../x/;           # "x123def";

$line =~ s/.../x/g;          # "xxx";


$line =~ s/(.)(.)/$2$1/;     # "bac123def"

$line =~ s/(.)(.)/$2$1/g;    # "ba1c32edf"
```



## Greedy quantifiers
{id: greedy-quantifiers}

![](examples/regex-perl/greedy.pl)

{aside}
/xa*/ on xaaab      xaaa  because it is greedy
/xa*/ on xabxaab    xa at the beginning even though the other  one is longer
/a*/  on xabxaab    the empty string at the beginning of the string
{/aside}


## minimal match
{id: minimal-match}

```
/a.*b/   axbzb
/a.*?b/  axbzb

/a.*b/
/a.*?b/
   axy121413413bq
   axyb121413413q
```


## Replace spaces
{id: replace-spaces}

```
s/^\s+//        leading
s/\s+$//        trailing
```


both ends:



```
s/^\s*(.*)\s*$/$1/   " abc " =>  "abc "  because of the greediness
```


```
s/^\s*(.*?)\s*$/$1/   " abc " =>  "abc"  minimal match
```


## Replace string in assembly code
{id: replace-string-in-assembly-code}
![](examples/regex-perl/assembly_source.txt)
![](examples/regex-perl/assembly_process.pl)


## Full example of previous
{id: replace-string-assembly-full}
![](examples/regex-perl/assembly_process_full.pl)


## split with regular expression
{id: split-with-regular-expression}

```
LIST = split REGEX, STRING;
```
![](examples/regex-perl/field_value_pairs.txt)
![](examples/regex-perl/parse_field_value_pairs.pl)


## Fixing dates
{id: fixing-date-with-regular-expression}


In the input we get dates like this
2010-7-5 but we would like to make sure we have two digits
for both days and months: 2010-07-05


![](examples/regex-perl/date.pl)
![](examples/regex-perl/date.out)
![](examples/regex-perl/date2.out)
![](examples/regex-perl/date3.out)



## Exercise: split CGI
{id: exercise-split-cgi}


Given a string that looks like this:



```
my $str = 'fname=Foo&amp;lname=Bar&amp;email=foo@bar.com';
```


Create a hash where the keys are fname, lname, email
or if the string looks like this



```
my $str = 'title=Stargates&amp;year=2005&amp;chapter=03&amp;bitrate=128';
```


then create a hash where the keys are title, year, chapter, bitrate
Use a single statement (with split) to achieve this.


![](examples/regex-perl/split_http_previous.pl)
![](examples/regex-perl/split_http.out)


## Exercise: basename/dirname
{id: exercise-basename-dirname}


Create two functions `basename()` and `dirname()`
Given a path such as `/home/foo/.mozilla/cache/data.txt`
the `basename()` function should return the filename ( data.txt in the example).
The `dirname()` function should return the full-path directory name
( `/home/foo/.mozilla/cache` in the example.)


## Exercise: Sort SNMP numbers
{id: exercise-sort-snmp-numbers}

Given a file with SNMP numbers (one number on every line)
print them in sorted order comparing the first number of
each SNMP number first.
If they are equal then comparing the second number, etc...



input:

![](examples/regex-perl/snmp.txt)

output:

![](examples/regex-perl/snmp.out)


## Exercise: parse hours log file and give report
{id: exercise-parse-log-file}


The log file looks like this


![](examples/regex-perl/timelog.log)

```
the report should look something like this:

09:20-11:00 Introduction
11:00-11:15 Exercises
11:15-11:35 Break
...


Solutions                   95 minutes   9%
Break                       65 minutes   6%
...
```


## Exercise: Parse ini file
{id: exercise-parse-ini-file}


An ini file has sections starting by the name of the section in square brackets and within
each section there are key = value pairs with optional spaces around the "=" sign.
The keys can only contain letters, numbers, underscore or dash.
In addition there can be empty lines and lines starting with # which are comments.




Given a filename, generate a 2 dimensional hash and then print it out with Data::Dumper.
Example ini file:


![](examples/regex-perl/inifile.ini)

Result

![](examples/regex-perl/inifile.out)


## Exercise: parse perl file
{id: exercise-parse-perl-file}


Parse your perl files and print out the names of your variables.
In the first version print out the scalar variables only.
In the second version show all variables.




The user gives the name of the file on the command line.

Input file:

![](examples/regex-perl/code_to_parse.pl)

Output:

![](examples/regex-perl/code_to_parse.out)



## Solution: Split CGI
{id: solution-split-cgi}

![](examples/regex-perl/split_cgi.pl)



## Solution: filename/dirname
{id: solution-basename-dirname}

![](examples/regex-perl/file_basename.pl)


## Solution: Sort SNMP numbers
{id: solution-sort-snmp-numbers}

![](examples/regex-perl/sort_snmp_numbers.pl)



## Solution: parse hours log file and give report
{id: solution-parse-log-file}

![](examples/regex-perl/timelog.pl)


## Solution: Parse ini file
{id: solution-parse-ini-file}

![](examples/regex-perl/parse_ini.pl)
![](examples/regex-perl/parse_ini_with_config_tiny.pl)


## Solution: parse perl file
{id: solution-parse-perl-file}

![](examples/regex-perl/print_variables.pl)


## Regular Expressions Cheat sheet
{id: regular-expressions-cheat-sheet}

|  Expression  |  Meaning  |
|    a         |  Just an 'a' character  |
|    .         |  any character except new-line  |
|    [bgh.]    |  one of the chars listed in the character class b,g,h or . |
|    [b-h]     |  The same as [bcdefgh]  |
|    [a-z]     |  Lower case letters  |
|    [b-]      |  The letter b or -  |
|    [^bx]     |  Anything except b or x  |
|    \w        |  Word characters: [a-zA-Z0-9_]  |
|    \d        |  Digits: [0-9]  |
|    \s        |  [\f\t\n\r ] form-feed, tab, newline, carriage return and SPACE |
|    \W        |  [^\w] |
|    \D        |  [^\d] |
|    \S        |  [^\s] |
|    [:class:] |  POSIX character classes (alpha, alnum...)  |
|    \p{...}   |  Unicode definitions (IsAlpha, IsLower, IsHebrew, ...) |
|    a*        |  0-infinite  'a' characters  |
|    a+        |  1-infinite  'a' characters  |
|    a?        |  0-1         'a' characters  |
|    a{n,m}    |  n-m         'a' characters  |
|    ( )       |  Grouping and capturing  |
|    |         |  Alternation  |
|    \1, \2    |  Capture buffers  |
|    $1, $2    |  Capture variables  |
|    ^ $       |  Beginning and end of string anchors  |


See also `perldoc perlre`

[Matching numbers using Perl regex](https://perlmaven.com/matching-numbers-using-perl-regex)






