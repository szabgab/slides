# Regular Expressions
{id: python-regular-expressions}

## What are Regular Expressions (aka. Regexes)?
{id: regexes}

* An idea on how to match some pattern in some text.
* A tool/language that is available in many places.
* Has many different "dialects"
* Has many different modes of processing.
* The grand concept is the same.
* Uses the following symbols:


```
() [] {} . * + ? ^ $ | - \ \d \s \w \A \Z \1 \2 \3
```


## What are Regular Expressions good for?
{id: regexes-used-for}

* Decide if a string is part of a larger string.
* Validate the format of some value (string) (e.g. is it a decimal number?, is it a hex?)
* Find if there are repetitions in a string.
* Analyze a string and fetch parts of if given some loose description.
* Cut up a string into parts.
* Change parts of a string.



## Examples
{id: regex-examples}

```
Is the input given by the user a number?

(BTW which one is a number:  23, 2.3,  2.3.4, 2.4e3, abc ?)

Is there a word in the file that is repeated 3 or more times?

Replaces all occurrences of Python or python by Java ...
... but avoid replacing Monty Python.


Given a text message fetch all the phone numbers:
Fetch numbers that look like 09-1234567
then also fetch +972-2-1234567
and maybe also 09-123-4567


Check if in a given text passing your network there are credit card numbers....


Given a text find if the word "password" is in it and fetch the surrounding text.


Given a log file like this:

[Tue Jun 12 00:01:00 2019] - (3423) - INFO - ERROR log restarted
[Tue Jun 12 09:08:17 2019] - (3423) - INFO - System starts to work
[Tue Jun 13 08:07:16 2019] - (3423) - ERROR - Something is wrong

provide statistics on how many of the different levels of log messages
were seen. Separate the log messages into files.
```


## Where can I use it ?
{id: where-are-regexes-used}

* grep, egrep
* Unix tools such as sed, awk, procmail
* vi, emacs, other editors
* text editors such as Multi-Edit
* .NET languages: C#, C++, VB.NET
* Java
* Perl
* **Python**
* PHP
* Ruby
* ...
* Word, Open Office ...
* PCRE



## grep
{id: grep}
{i: grep}

{aside}

**grep** gets a regex and one or more files. It goes over line-by-line all the files and displays the lines where the regex matched. A few examples:
{/aside}

```
grep python file.xml    # lines that have the string python in them in file.xml.
grep [34] file.xml      # lines that have either 3 or 4 (or both) in file.xml.
grep [34] *.xml         # lines that have either 3 or 4 (or both) in every xml file.
grep [0-9] *.xml        # lines with a digit in them.
egrep '\b[0-9]' *.xml   # only highlight digits that are at the beginning of a number.
```



## Regexes first match
{id: regexes-first-match}
{i: r}
{i: re}
{i: search|re}
{i: group|re}
![](examples/regex/search.py)

{aside}

The search method returns an object or **None**, if it could not find any match.
If there is a match you can call the **group()** method. Passing 0 to it will
return the actual substring that was matched.
{/aside}


## Match numbers
{id: match-numbers}
{i: r|re}
{i: \d}
{i: group|re}

![](examples/regex/match_numbers.py)

Use raw strings for regular expression: r'a\d'. Especially because \ needs it.


* \d matches a digit.
* + is a quantifier and it tells \d to match one or more digits.



It matches the first occurrence.
Here we can see that the `group(0)` call is much more interesting than earlier.


## Capture
{id: capture}
{i: ()|re}

![](examples/regex/capture.py)

{aside}
Parentheses in the regular expression can enclose any sub-expression.
Whatever this sub-expression matches will be saved and can be accessed using the group() method.
{/aside}


## Capture more
{id: capture-more}
{i: ()|re}
{i: \w|re}

![](examples/regex/capture_more.py)

{aside}
Some groups might match '' or even not match at all, in which case we get None
in the appropriate match.group() call and in the match.groups() call
{/aside}


## Capture even more
{id: capture-even-more}

![](examples/regex/capture_even_more.py)


## findall
{id: findall}
{i: findall}

![](examples/regex/findall.py)

**re.findall** returns the matched substrings.


## findall with capture
{id: findall-capture}
{i: findall}

![](examples/regex/findall_capture.py)


## findall with capture more than one
{id: findall-capture-more}

![](examples/regex/findall_capture_more.py)

{aside}
If there are multiple capture groups then The returned list will consist of tuples.
{/aside}


## Any Character
{id: any-character}
{i: .}

**.** matches any one character except newline.


For example: **#.#**

![](examples/regex/any_character.py)

If **re.DOTALL** is given newline will be also matched.



## Match dot
{id: match-dot}
{i: .}
{i: \}

![](examples/regex/match_dot.py)


## Character classes
{id: character-classes}
{i: []}
{i: -}


We would like to match any string that has any of the #a#, #b#, #c#, #d#, #e#, #f#, #@# or #.#


![](examples/regex/character_class.py)

```
r'#[abcdef@.]#'
r'#[a-f@.]#'
```


## Common characer classes
{id: commont-character-classes}
{i: \d}
{i: \w}
{i: \s}

* **\d** digit: `[0-9]` or [Unicode Characters in the 'Number, Decimal Digit' Category](https://www.fileformat.info/info/unicode/category/Nd/list.htm)
* **\w** word character `[a-zA-Z0-9_]` (digits, letters, underscore) or see the Unicode set of digits and letters
* **\s** white space: `[\f\t\n\r ]` form-feed, tab, newline, carriage return and SPACE

* Usast: stand alone: \d or as part of a larger character class: [abc\d]

## Match digits
{id: match-digits}

![](examples/regex/digits.py)
![](examples/regex/digits.out)

## Word Characters
{id: word-characters}

![](examples/regex/word_characters.py)
![](examples/regex/word_characters.out)

## Negated character class
{id: negated-character-class}
{i: \D}
{i: \W}
{i: \S}

* **[^abc]** matches any one character that is not 'a', not 'b' and not 'c'.
* \D not digit [^\d]
* \W not word character [^\w]
* \S not white space [^\s]


## Optional character
{id: regex-optional}
{i: ?}

Match the word **color** or the word **colour**

```
Regex: r'colou?r'
```

```
Input: color
Input: colour
Input: colouur
```


## Regex 0 or more quantifier
{id: regex-quantifiers}
{i: *}

Any line with two - -es with anything in between.

```
Regex: r'-.*-'
Input: "ab"
Input: "ab - cde"
Input: "ab - qqqrq -"
Input: "ab -- cde"
Input: "--"
```


## Quantifiers
{id: quantifiers}
{i: quantifiers}
{i: ?}
{i: +}
{i: *}


Quantifiers apply to the thing in front of them



```
r'ax*a'      # aa, axa, axxa, axxxa, ...
r'ax+a'      #     axa, axxa, axxxa, ...
r'ax?a'      # aa, axa
r'ax{2,4}a'  #          axxa, axxxa, axxxxa
r'ax{3,}a'   #                axxxa, axxxxa, ...
r'ax{17}a'   #                                 axxxxxxxxxxxxxxxxxa
```
|  *  |  0-   |
|  +  |  1-   |
|  ?  |  0-1  |
|  {n,m}  |  n-m  |
|  {n,}  |  n-  |
|  {n}  |  n  |


## Quantifiers limit
{id: quantifiers-limit}
![](examples/regex/quantifier_limit.py)


## Quantifiers on character classes
{id: quantifiers-on-character-class}
![](examples/regex/quantifier_on_character_class.py)


## Greedy quantifiers
{id: greedy-quantifiers}
![](examples/regex/greedy.py)

{aside}

They match 'xaaa', 'xa' and '' respectively.
{/aside}


## Minimal quantifiers
{id: minimal-quantifiers}
![](examples/regex/minimal.py)


## Anchors
{id: anchors}
{i: \A}
{i: \Z}
{i: ^}
{i: $}

* \A matches the beginning of the string
* \Z matches the end of the string
* ^ matches the beginning of the row (see also re.MULTILINE)
* $ matches the end of the row but will accept a trailing newline (see also re.MULTILINE)

![](examples/regex/anchors.py)
![](examples/regex/anchors.out)


## Anchors on both end
{id: anchors-both-end}
![](examples/regex/anchors_both.py)
![](examples/regex/anchors_both.out)

## Anchor edge of word
{id: anchor-edge-of-word}
{i: \b}

* \b beginning of word or end of word

![](examples/regex/anchors_b.py)
![](examples/regex/anchors_b.out)

## Match ISBN numbers
{id: matching-isbn}

```
```
![](examples/regex/isbn.py)


## Matching a section
{id: matching-section}
![](examples/regex/matching_section.py)


## Matching a section - minimal
{id: matching-section-minimal}
![](examples/regex/matching_section_minimal.py)



## Matching a section negated character class
{id: matching-section-with-negated-character-class}
![](examples/regex/negated_character_class.py)


## DOTALL S (single line)
{id: dotall}
{i: .}
{i: DOTALL}
{i: S}

if re.DOTALL is given, . will match any character. Including newlines.

![](examples/regex/dotall.py)


## MULTILINE M
{id: multiline}
{i: ^}
{i: $}
{i: MULTILINE}
{i: M}

if re.MULTILNE is given, ^ will match beginning of line and $ will match end of line

![](examples/regex/multiline.py)

```
line
----------
line
text
```

```
re.MULTILINE | re.DOTALL
```


## Two regex with logical or
{id: regexes-with-logical-or}


All the rows with either 'apple pie' or 'banana pie' in them.


![](examples/regex/alternatives.py)


## Alternatives
{id: regex-alternatives}
{i: |}

Alternatives

![](examples/regex/alternatives_in_regex.py)


## Grouping and Alternatives
{id: regex-grouping-alternatives}
{i: ()}


Move the common part in one place and limit the alternation
to the part within the parentheses.


![](examples/regex/alternatives_with_grouping.py)



## Internal variables
{id: internal-variables}
{i: \1}
{i: \2}
{i: \3}
{i: \4}
![](examples/regex/same_character.py)


## More internal variables
{id: internal-variables-more}
{i: \1}

```
(.)(.)\2\1

(\d\d).*\1

(\d\d).*\1.*\1

(.{5}).*\1
```


## Regex DNA
{id: regex-dna}

* DNA is built from G, A, T, C
* Let's create a random DNA sequence
* Then find the longest repeated sequence in it

![](examples/regex/dna.py)


## Regex IGNORECASE
{id: regex-ignorecase}
{i: IGNORECASE}
{i: I}
![](examples/regex/ignorecase.py)


## Regex VERBOSE X
{id: regex-verbose}
{i: VERBOSE}
{i: X}
![](examples/regex/verbose.py)


## Substitution
{id: substitution}
![](examples/regex/substitution.py)


## findall capture
{id: findall-capture-examples}
{i: findall}

If there are parentheses in the regex, it will return tuples of the matches

![](examples/regex/findall_capture_examples.py)


## Fixing dates
{id: fixing-date-with-regular-expression}


In the input we get dates like this
2010-7-5 but we would like to make sure we have two digits
for both days and months: 2010-07-05


![](examples/regex/date.py)
![](examples/regex/date.out)


## Duplicate numbers
{id: duplicate-numbers}
![](examples/regex/duplicate_numbers.py)


## Remove spaces
{id: remove-spaces}
![](examples/regex/remove_spaces.py)


## Replace string in assembly code
{id: replace-string-in-assembly-code}
![](examples/regex/assembly_source.txt)
![](examples/regex/assembly_process.py)
![](examples/regex/assembly_process_dict.py)
![](examples/regex/assembly_process_dict2.py)
![](examples/regex/assembly_process_generate.py)


## Full example of previous
{id: replace-string-assembly-full}

![](examples/regex/assembly_process_full.py)


## Split with regex
{id: split-with-regex}
![](examples/regex/field_value_pairs.txt)
![](examples/regex/parse_field_value_pairs.py)
![](examples/regex/field_value_pairs.out)


## Exercises: Regexes part 1
{id: exercises-regexes-1}


Pick up a file with some text in it.  Write a script (one for each item) that prints out every line from the file
that matches the requirement.  You can use the script at the end of the page as a starting point but you will
have to change it!



* has a 'q'
* starts with a 'q'
* has 'th'
* has an 'q' or a 'Q'
* has a '*' in it
* starts with an 'q' or an 'Q'
* has both 'a' and 'e' in it
* has an 'a' and somewhere later an 'e'
* does not have an 'a'
* does not have an 'a' nor 'e'
* has an 'a' but not 'e'
* has at least 2 consecutive vowels (a,e,i,o,u) like in the word "bear"
* has at least 3 vowels
* has at least 6 characters
* has at exactly 6 characters
* all the words with either 'Bar' or 'Baz' in them
* all the rows with either 'apple pie' or 'banana pie' in them
* for each row print if it was apple or banana pie?
* Bonus: Print if the same word appears twice in the same line
* Bonus: has a double character (e.g. 'oo')

![](examples/regex/regex_exercise.py)


## Exercise: Regexes part 2
{id: exercises-regexes-2}


Write functions that returns true if the given value is a



* Hexadecimal number
* Octal number
* Binary number



Write a function that given a string it return true if the string is a number.
As there might be several definitions of what is the number create several solutions
one for each definition:



* Non negative integer.
* Integer. (Will you also allow + in front of the number or only - ?
* Real number. (Do you allow .3 ? What about 2. ?
* In scientific notation. (something like this: 2.123e4 )

![](examples/regex/which_are_numbers.txt)


## Exercise: Sort SNMP numbers
{id: exercise-sort-snmp-numbers}


Given a file with SNMP numbers (one number on every line)
print them in sorted order comparing the first number of
each SNMP number first.
If they are equal then comparing the second number, etc...



input:

![](examples/regex/snmp.txt)

output:

![](examples/regex/sorted_snmp.txt)


## Exercise: parse hours log file and give report
{id: exercise-parse-log-file}


The log file looks like this


![](examples/regex/timelog.log)


the report should look something like this:


![](examples/regex/timelog.txt)


## Exercise: Parse ini file
{id: exercise-parse-ini-file}


An ini file has sections starting by the name of the section in square brackets and within
each section there are key = value pairs with optional spaces around the "=" sign.
The keys can only contain letters, numbers, underscore or dash.
In addition there can be empty lines and lines starting with # which are comments.

Given a filename, generate a 2 dimensional hash and then print it out.
Example ini file:

![](examples/regex/inifile.ini)

If you print it, it should look like this (except of the nice formatting).

![](examples/regex/inifile.out)


## Exercise: Replace Python
{id: exercise-replace-python}

![](examples/regex/text_with_python.txt)


## Exercise: Extract phone numbers
{id: exercise-phone-number}

![](examples/regex/phone.txt)



## Solution: Sort SNMP numbers
{id: solution-sort-snmp-numbers}

![](examples/regex/sort_snmp.py)


## Solution: parse hours log file and give report
{id: solution-parse-log-file}

![](examples/regex/timelog.py)



## Solution: Processing INI file manually
{id: solution-processing-ini-file-manually}

![](examples/other/data.ini)
![](examples/other/ini_parser.py)


## Solution: Processing config file
{id: solution-config-parsing}
{i: ConfigParser}

![](examples/other/data_clean.ini)
![](examples/other/config_parsing.py)


## Solution: Extract phone numbers
{id: solution-phone-number}

![](examples/regex/phone.py)



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
|    a*        |  0-infinite  'a' characters  |
|    a+        |  1-infinite  'a' characters  |
|    a?        |  0-1         'a' characters  |
|    a{n,m}    |  n-m         'a' characters  |
|    ( )       |  Grouping and capturing  |
|    |         |  Alternation  |
|    \1, \2    |  Capture buffers  |
|    ^ $       |  Beginning and end of string anchors  |


[re](http://docs.python.org/library/re.html)




## Fix bad JSON
{id: fix-bad-json}
![](examples/regex/bad.json)
![](examples/regex/read_json.py)
![](examples/regex/read_json_fixed.py)


## Fix very bad JSON
{id: fix-very-bad-json}
![](examples/regex/very_bad.json)
![](examples/regex/fix_very_bad_json.py)


## Raw string or escape
{id: raw-string-or-escape}
{i: \}
{i: r}

Let's try to check if a string contains a back-slash?

![](examples/regex/escape.py)


## Remove spaces regex
{id: remove-spaces-regex}


This is not necessary as we can use rstrip, lstrip, and replace.


![](examples/regex/remove_spaces_regex.py)


both ends:



```
re.sub(r'\s*(.*)\s*$', r'\1', line)  #  " abc " =>  "abc "  because of the greediness
```


```
re.sub('^\s*(.*?)\s*$', '\1', line)  #   " abc " =>  "abc"  minimal match
```


## Regex Unicode
{id: regex-unicode}


Python 3.8 required


![](examples/regex/print_unicode.py)
![](examples/regex/mixed.txt)
![](examples/regex/match_unicode.py)


## Anchors Other example
{id: anchors-other}
{i: \A}
{i: \Z}
{i: ^}
{i: $}
![](examples/regex/other_anchors.py)




