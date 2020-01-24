# Regular Expressions II
{id: regex2}


## Grouping, alternatives
{id: regex-grouping-alternatives}

all the rows with either 'apple pie' or 'banana pie' in them

```
if ($row =~ /apple pie/ or $row =~ /banana pie/) {
}
```

Alternatives


```
if ($row =~ /apple pie|banana pie/) {
}
```


Move the common part in one place and limit the alternation
to the part within the parentheses.



```
if ($row =~ /(apple|banana) pie/) {
}
```


## Capturing
{id: regex-capturing}
{i: \1}
{i: $1}
{i: ()}
{i: capturing}
{i: grouping}

```
if ($row =~ /(apple|banana) pie/) {
    print $1;
}
```

```
Has a double character (e.g. 'oo' in loop)
```

```
# Input:   "my loop"

if ($line =~ /(.)\1/) {
    print $1;
}
```

```
Print if the same word appears twice in the same line
```

```
my $str = " in this line there is this word twice ";
if ($str =~ / ([a-z]+) .* \1 /) {
    print "$1\n";
}
```

```
/(.+).*\1/        # lines with anything more than once
/((.+).*\1)+/     # Syntax error ! Why ?

if ($line =~ /(.*)=(.*)/) {
    print "left:  $1\n";
    print "right: $2\n";
}
```


## Anchors
{id: regex-anchors}
{i: anchors}
{i: ^}
{i: $}
{i: \b}

```
^            # at the beginning of the pattern means beginning of the string
$            # at the end of the pattern means the end of the string

/the/        # matches anywhere in the string:             
             # "atheneum", "thermostat", "the", "mathe"
			 
/^the/       # matches only if the string starts with the
             # "thermostat", "the"
			 
/the$/       # matches only if the string ends with the
             # "the", "mathe"
			 
/^the$/      # matches only if the string
             # "the"

/^The.*finished$/
             # starts with  "The" ends with "finished" and anything in between


\b           # Word delimiter
/\bstruct\b/ # match every place the word "struct" but not 
             # "structure" or "construct"
```


## Character classes
{id: regex-character-classes}


A list of optional characters within square brackets []




```
/a[bc]a/      # aba, aca
/a[2#=x?.]a/  # a2a, a#a, a=a, axa, a?a, a.a
              # inside the character class most of the spec characters lose their
              # special meaning  BUT there are some new special characters
/a[2-8]a/     # is the same as /a[2345678]a/
/a[2-]a/      # a2a, a-a        - has no special meaning at the ends
/a[-8]a/      # a8a, a-a
/a[6-C]a/     # a6a, a7a ... aCa
              #      characters from the ASCII table: 6789:;&lt;=&gt;?@ABC
/a[C-6]a/     # syntax error 

/a[^xa]a/     # "aba", "aca"  but not "aaa", "axa"    what about "aa" ?
              # ^ as the first character in a character class means 
              # a character that is not in the list
/a[a^x]a/     # aaa, a^a, axa
```


## Special character classes
{id: regex-special-character-classes}
{i: \w}
{i: \d}
{i: \s}
{i: ^}
{i: $}

|  Expression  |  Meaning  | Usage |
|    \w        |  Word characters: [a-zA-Z0-9_] | \w+ or [\w#-]+ |
|    \d        |  Digits: [0-9]  |  |
|    \s        |  [\f\t\n\r ] form-feed, tab, newline, carriage return and SPACE |  |
|    \W        |  [^\w] |  |
|    \D        |  [^\d] |  |
|    \S        |  [^\s] |  |
|    [:class:] |  POSIX character classes (alpha, alnum...)  | [:alpha:]+  or  [[:alpha:]#-]+ |
|    \p{...}   |  Unicode definitions (IsAlpha, IsLower, IsHebrew, ...) | \p{IsHebrew}+   or [\p{IsHebrew}#!-] |
|    \P{...}   |  Negation of Unicode character class |  |


See also `perldoc perlre` and `perldoc perluniintro`.


## Exercise: Hex/Oct/Bin
{id: exercise-hex-oct-bin}


Write functions that return true if the given value is a



* Hexadecimal number
* Octal number
* Binary number



## Exercise: Number
{id: exercise-number}


Write a function that given a string it return true if the string is a number.
As there might be several definitions of what is the number create several solutions
one for each definition:



* Non negative integer.
* Integer. (Will you also allow + in front of the number or only - ?
* Real number. (Do you allow .3 ? What about 2. ?
* In scientific notation. (something like this: 2.123e4 )



## Exercise: Roman numbers
{id: exercise-roman-numbers}


Write functions that return true if the given value is a Roman Number.
If you can do that maybe write another function to return the decimal
value of the given number.



```
I, II, III, IV, V, VI, VII,....
   I = 1
   V = 5
   X = 10
   L = 50
   C = 100
   D = 500
   M = 1000
```


## Solution: Number
{id: solution-number}
![](examples/regex/is_number.pl)


## Solution: Hex/Oct/Bin
{id: solution-hex-oct-bin}
![](examples/regex/is_base_number.pl)


## Solution: Roman numbers
{id: solution-roman-numbers}
![](examples/regex/is_roman_number.pl)




