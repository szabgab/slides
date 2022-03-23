# Regular Expressions - part 3
{id: regex-3}


## Two regex with logical or
{id: regexes-with-logical-or}

All the rows with either 'apple pie' or 'banana pie' in them.

![](examples/regex/alternatives.py)
![](examples/regex/alternatives.out)


## Alternatives
{id: regex-alternatives}
{i: |}

Alternatives

![](examples/regex/alternatives_in_regex.py)
![](examples/regex/alternatives_in_regex.out)


## Grouping and Alternatives
{id: regex-grouping-alternatives}
{i: ()}

Move the common part in one place and limit the alternation
to the part within the parentheses.

![](examples/regex/alternatives_with_grouping.py)
![](examples/regex/alternatives_with_grouping.out)


## Internal variables
{id: internal-variables}
{i: \1}
{i: \2}
{i: \3}
{i: \4}

![](examples/regex/same_character.py)
![](examples/regex/same_character.out)


## More internal variables
{id: internal-variables-more}
{i: \1}

![](examples/regex/internal_variables.py)


## Regex DNA
{id: regex-dna}

* DNA is built from G, A, T, C
* Let's create a random DNA sequence
* Then find the longest repeated sequence in it

![](examples/regex/dna.py)
![](examples/regex/dna.out)


## Regex IGNORECASE
{id: regex-ignorecase}
{i: IGNORECASE}
{i: I}
![](examples/regex/ignorecase.py)

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

## Combine Regex flags
{id: combine-regex-flags}
{i: |}

* Use the bitwise or for that.

```
re.MULTILINE | re.DOTALL
```

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


## Double numbers
{id: double-numbers}

{aside}
We have a string that has some numbers in it. We would like to double the numbers.

In the first example we can see a relatively simple way of doubling the numbers. We captuter a number using the `(\d+)` expression
that will save the current number in `\1` and then we include it twice: `\1\1`. This will convert a number like 1 to 11.
This is nice, but probably not what we wanted. We wanted to convert 1 to 2 and 34 to 68.

We can't do that with plain regular expressions and substitutions as that is all string-based. The plain substitution can only move around characters,
but it cannot do any complex operations on the and thus cannot compute anything.

However, if the substitution part is a function then Python will call that function passing in the match object and whatever the function returns will
be the replacement string. This function can be a regular function defined with `def` or a `lambda` expression.

In the second example we see the solution with `lambda`-expression.

The 3rd examples is the same solution but in a very step-by-step way with lots of temporary variables. This will hopefully help understand the
`lambda`-expression in the 2nd example.
{/aside}


![](examples/regex/duplicate_numbers.py)


## Remove spaces
{id: remove-spaces}
![](examples/regex/remove_spaces.py)


## Replace string in Assembly code
{id: replace-string-in-assembly-code}

{aside}
At a company we had some Assembly code that looks like the text file. In case you don't know, [Assembly](https://en.wikipedia.org/wiki/Assembly_language) is
a very low level programming language. Here we have some sample code that uses variables like A and registers like R1, R2, and R3.

We had this code, but because the hardware changed we had to make changes to the code and rename the registies R1 to be R2, R2 to be R3, and R3 to be R1.
We cannot just simple do these steps one after the other becasue once we renamed R1 to be R2 we won't know which of the R2-s do we need to rename and which
are new. So someone came up with the idea to use R4 as a temporary name and start by renaming R1 to R4,  R3 to R1, R2 to R3, and finally the temporary R4 to R2.

As you could see in our solution coed.

It worked all very smoothly till we turned on the device that immediately emitted smoke. It did not pass the "smoke test".

As it turns out in the original text there were also R4 registers that we have not noticed and they were all renamed to be R2.

The first idea to improve our converter program was to use some other temporary string that for sure cannot be in the code, such as QQRQ, but then
we arrived to the conclusion that there are better ways to solve this.
{/aside}

![](examples/regex/assembly_source.txt)

![](examples/regex/assembly_process.py)

## Replace string in Assembly code - using mapping dict
{id: replace-string-in-assembly-code-using-mapping-dict}

{aside}
The first imprvement was to create a dictionary with the mapping from old string to new string
and then have a regex that will match exactly the 3 possible original string. In the substitute
part we'll have to use a function as we need the current matching object to access the current match.

The function can be either a `lambda`-expression as in the first solution or a fully defined function
as in the seconde solution that I added only to make it easier to understand the first solution.

This is a nice and working solution, but it has two issues.

In the regex used a character class because we assumed that there are only going to be on-digit registries.
If you look at the original Assembly code you can see there are also R12 and R21.

In addition we now have data duplication. If we change the mapping adding a new original string or removing one,
we'll also have to remember to update the regex. It is not DRY.
{/aside}


![](examples/regex/assembly_process_dict.py)

## Replace string in Assembly code - using alternatives
{id: replace-string-in-assembly-code-using-alternatives}

{aside}
We can solve the first issue by changing the regex. Instead of using a character class, we use alternatives (vertical line, aka. pipe)
and fully write down the original strings.

The rest of the code is the same and the second issue is not solved yet, we still have to make sure the keys of the dictionary and the values
in the regex are the same.

However this solution makes it easier to solve the second issue as well.
{/aside}

![](examples/regex/assembly_process_dict2.py)

## Replace string in Assembly code - generate regex
{id: replace-string-in-assembly-code-generate-regex}

{aside}
In this solution we generate the regex from the keys of the mapping dictionary.

Once we have this we also opened other opportunities for improvement. Now that all the replacement mapping
comes from a regex we have separated the "data" from the "code". We can now decide to read in the mapping
from an Excel file (for example). That way we can hand over the mapping creation to someone who does not know
Python. Our code will take that file, read the mapping from the spreadsheet, create the mapping dictionary,
create the regex and do the work.
{/aside}

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


## Exercise: parse hours log file and create report
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

Write a script called **replace_python.py** that given a file will replace all occurrences of "Python" or "python" by Java,
but will avoid replacing the word in Monty Python. It prints the resulting rows to the screen.

For example given the input:

![](examples/regex/text_with_python.txt)

Will print:

![](examples/regex/text_with_java.txt)

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




