# Regular Expressions
{id: regex}

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

(BTW which one is a number:  23, 2.3, .3, 2., 2.3.4.7.12, 2.4e3, abc ?)

Is there a substring in the file that is repeated 3 or more times?

Replaces all occurrences of Python or python by Java ...
... but avoid replacing Monty Python.


Given a text message fetch all the phone numbers:
Fetch numbers that look like 09-1234567
then also fetch +972-2-1234567
and maybe also 09-123-4567
but this #456 is not a phone number


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

## Named capture
{id: named-capture}
{i: \P}
{i: P}

![](examples/regex/named_capture.py)

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
* **\s** white space: `[\f\t\n\r\v ]` form-feed, tab, newline, carriage return, vertical-tab, and SPACE

* Use stand alone: \d or as part of a larger character class: [abc\d]

## Negated character class
{id: negated-character-class}
{i: \D}
{i: \W}
{i: \S}

* **[^abc]** matches any one character that is not 'a', not 'b' and not 'c'.
* \D not digit [^\d]
* \W not word character [^\w]
* \S not white space [^\s]

## Character classes summary
{id: character-classes-summary}

```
a[bc]a      # aba, aca
a[2#=x?.]a  # a2a, a#a, a=a, axa, a?a, a.a
            # inside the character class most of the spec characters lose their
            # special meaning  BUT there are some new special characters
a[2-8]a     # is the same as /a[2345678]a/
a[2-]a      # a2a, a-a        - has no special meaning at the ends
a[-8]a      # a8a, a-a
a[6-C]a     # a6a, a7a ... aCa
              #      characters from the ASCII table: 6789:;&lt;=&gt;?@ABC
a[C-6]a     # Error: "bad character range"

a[^xa]a     # "aba", "aca"  but not "aaa", "axa"    what about "aa" ?
              # ^ as the first character in a character class means 
              # a character that is not in the list
a[a^x]a     # aaa, a^a, axa
```

## Character classes and Unicode characters
{id: character-classes-unicode-characters}

![](examples/regex/character_class_unicode.py)

## Character classes for Hebrew text
{id: character-classes-for-hebrew-text}

![](examples/regex/character_class_hebrew.py)

## Match digits
{id: match-digits}

![](examples/regex/digits.py)
![](examples/regex/digits.out)

## Word Characters
{id: word-characters}

![](examples/regex/word_characters.py)
![](examples/regex/word_characters.out)

## Exercise: add numbers
{id: exercise-add-numbers}

Given a file like this:

![](examples/regex/grades1.txt)

* Add up the scores for each name and print the result.

```
Foo   : 79
Bar   : 31
Zorg  :  7
```

* Make it work also on a file that looks like this:

![](examples/regex/grades2.txt)


## Solution: add numbers
{id: solution-add-numbers-1}

![](examples/regex/grades1.py)

## Solution: add numbers
{id: solution-add-numbers-2}

![](examples/regex/grades2.py)

## Solution: add numbers
{id: solution-add-numbers-3}

![](examples/regex/grades3.py)

