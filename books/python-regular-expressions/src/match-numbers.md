# Match numbers

r|re
\d
group|re

{% embed include file="src/examples/regex/match_numbers.py" %}

Use raw strings for regular expression: r'a\d'. Especially because \ needs it.


* \d matches a digit.
* + is a quantifier and it tells \d to match one or more digits.



It matches the first occurrence.
Here we can see that the `group(0)` call is much more interesting than earlier.



