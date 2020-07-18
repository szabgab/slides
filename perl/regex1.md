# Regular Expressions I
{id: regex1}


## What are regexes good for ?
{id: regexes}

* Decide if a string is part of a larger string
* Validate the format of some value (string) (e.g. is it a decimal number?, is it a hex?)
* Find if there are repetitions in a string
* Analyze a string and fetch parts of if given some loose description


## Examples
{id: regex-examples}

```
Is the input given by the user a number?

(BTW which one is a number:  23, 2.3,  2.3.4, 2.4e3, abc ?)

Is there a word in the file that is repeated 3 or more times?

Replaces all occurrences of Perl or perl by Java ...
... but avoid replacing Perla.


Given a text message fetch all the phone numbers:
Fetch numbers that look like 09-1234567
then also fetch +972-2-1234567
and maybe also 09-123-4567

Check if in a given text passing your network there are credit card numbers....

Given a text find if the word "password" is in it and fetch the surrounding text.

Given a log file like this:

[Tue Jun 12 00:01:00 2006] - (3423) - INFO - ERROR log restarted
[Tue Jun 12 09:08:17 2006] - (3423) - INFO - System starts to work
[Tue Jun 13 08:07:16 2006] - (3423) - ERROR - Something is wrong

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
* PHP, Python, Ruby, Tcl
* Word, Open Office ...
* PCRE




## Introduction to Regexes
{id: introduction-to-regexes}
{i: =~}
{i: !~}
{i: //}

```
my $str = "Some string here";
if ($str =~ /m/) {
    print "There is a match\n";
}

if ($str !~ /a/) {
    print "No match\n";
}

# which is the same as

if (not $str =~ /a/) {
    print "No match\n";
}
```


## grep
{id: grep}
{i: grep}

The Unix(ish) grep command was named after the `g/re/p` command of the UNIX ed editor.

```
$ grep REGEX file(s)
```


## Tools
{id: regex-tools}

Linux

* kregexpeditor
* regexxer

Windows

* [Regex Coach](http://weitz.de/regex-coach/)

Commercial on Windows

* [Regex Buddy](http://www.regexbuddy.com/) teaching Regex
* [Power Grep](http://www.powergrep.com/) grep with gui

Both Linux and Windows

* [ack](https://metacpan.org/pod/ack)
* [Padre](https://metacpan.org/pod/Padre)


## Find a string in a file
{id: grep-like-perl}

![](examples/regex-perl/find_string.pl)


## Regex Examples: single character
{id: regex-single-characters}


Any line that has an 'x' in it.



```
Regex: /x/
Input: "abcde"
Input: "abxcde"
Input: "xabcde"
Input: "xabcxde"
```



Any line that starts with an 'x'.



```
Regex: /^x/
Input: "abcde"
Input: "abxcde"
Input: "xabcde"
Input: " xabcde"
Input: "^xabcde"
```


^ at the beginning of the regular expression means, match at the beginning of the string.




## Regex Examples: more characters
{id: regex-more-characters}


Any line that has an 'abc' in it.



```
Regex: /abc/
Input: "abc xy"
Input: "abcde"
Input: "abxcxbdabce"
Input: "xabcde"
Input: "xa b c de"
```



Any line that starts with an 'abc'.



```
Regex: /^abc/
Input: "abcde"
Input: "abxcxbde"
Input: "xabcde"
```


## Regex Examples dot .
{id: regex-dot}


Any line that has any of the xax, xbx, ...,
that is any character between two x-es.



```
Regex: /x.x/
Input: "abcde"
Input: "abxcxbde"
Input: "xabcde"
Input: "xabxcxde"
Input: "adax xabcde"
Input: "adax.xabcde"
Input: "x.x"
Input: "xx"
```


Only lines that have x.x (A real . between two x-es.)



```
Regex: /x\.x/  
```

```
The special characters are: . * + ? ^ $ \ ( ) [ ] | { }    and the delimiter: /

Some of the characters change their special meaning based on position. 
```


## Regex Examples (character class)
{id: regex-character-class}


Any line that has any of the #a#, #b#, #c#, #d#, #e#, #f#, #@# or #.#



```
Regex: /#[abcdef@.]#/
Input: "ab #q# "
Input: "ab #z#a# "
Input: "ab #.# "
Input: "ab ## "
Input: "#a#"
Input: "##"
Input: "###"
```

```
Regex: /#[a-f@.]#/ 
```


## Regex Examples (^ in character class)
{id: caret-in-character-class}


^ as the first character in a character class means
  "a character that is not listed in this character class"



```
Regex: /#[^abc]#/
Input: "abc #a# z"
Input: "abc #z# z"
Input: "#z#"
Input: "##"
```


## Optional character
{id: regex-optional}
{i: ?}

Match the word **color** or the word **colour**.

```
Regex: /colou?r/
```

```
Input: color
Input: colour
Input: colouur
```


## Regex Examples quantifiers
{id: regex-quantifiers-example}
{i: quantifiers}
{i: ?}
{i: +}
{i: *}


Any line with two - -es with anything in between.



```
Regex: /-.*-/
Input: "ab"
Input: "ab - cde"
Input: "ab - qqqrq -"
Input: "ab -- cde"
Input: "--"
```


## Quantifiers
{id: regex-quantifiers}


Quantifiers apply to the thing in front of them



```
/ax*a/      # aa, axa, axxa, axxxa, ...
/ax+a/      #     axa, axxa, axxxa, ...
/ax?a/      # aa, axa
/ax{2,4}a/  #          axxa, axxxa, axxxxa
/ax{3,}a/   #                axxxa, axxxxa, ...
/ax{17}a/   #                                 axxxxxxxxxxxxxxxxxa
```

```
*      0-
+      1-
?      0-1
{n,m}  n-m
{n,}   n-
{n}    n
```


## Quantifiers on character classes
{id: regex-quantifiers-on-character-class}

```
Regex: /-[abc]-/
Input: "-a-"
Input: "-b-"
Input: "-x-"
Input: "-ab-"
```

```
Regex: /-[abc]+-/
Input: "-a-"
Input: "-b-"
Input: "-aa-"
Input: "-ab-"
Input: "-x-"
Input: "--"
```



## Exercises: Regular expressions
{id: exercise-regular-expressions}


Pick up a file with some text in it.  (e.g. examples/regex-perl/text.txt ).
Write a script (one for each item) that prints out every line from the file
that matches the requirement.
You can use the script at the end of the page as a starting point but you will
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

![](examples/regex-perl/regex_exercise.pl)


## Solutions: Regular expressions
{id: solution-regular-expressions}

* has a 'q' `/q/`
* starts with a 'q' `/^q/`
* has 'th' `/th/`
* has an 'q' or a 'Q' `/[qQ]/`
* has a `*` in it `/\*/`
* another solution: `/[*]/`
* starts with an 'q' or an 'Q' `/^[qQ]/`
* has both 'a' and 'e' in it `$str =~ /a/ and $str =~ /e/`
* has an 'a' and somewhere later an 'e' `/a.*e/`
* does not have an 'a' `$str !~ /a/`  Not good: `/[^a]/`
* does not have an 'a' nor 'e' `$str !~ /[ae]/`
* has an 'a' but not 'e' **$str =~ /a/ and $str !~ /e/**
* has at least 2 consecutive vowels (a,e,i,o,u) like in the word "bear" **/[aeiou]{2}/**
* has at least 3 vowels  **/[aeiou].*[aeiou].*[aeiou]/**
* has at least 6 characters **/....../**
* another solution: **/.{6}/**
* yet another solution: **length($str) >= 6**
* has at exactly 6 characters: **length($str) == 6**
* all the words with either 'Bar' or 'Baz' in them  **/Ba[rz]/**
* all the rows with either 'apple pie' or 'banana pie' in them `if ($row =~ /apple pie/ or $row =~ /banana pie/){ }`
* for each row print if it was apple or banana pie?


```
my $ok;
if ($row =~ /apple pie/) {
     print "apple\n";
     $ok = 1;
} elsif ($row =~ /banana pie/) {
     print "banana\n";
     $ok = 1;
}
```



