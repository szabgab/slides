# Exercise: print lines with Report



In many cases you get some text report in some free form of text (and not in a CSV file or an Excel file.) You need to extract the information
from such a file after recognizing the patterns. This exercise tries to provide such a case.

* Create a script called **text_report.py**

Given a file that looks like this:

{% embed include file="src/examples/files/text_report.txt" %}

* Print out the first line that starts with `Report:`.
* Print out all the lines that have the string `Report:` in it.
* Print out all the lines that start with the string `Report:`.
* Print out the numbers that are after `Report:`. (e.g. `Report: 42` print out 42)
* Add the numbers that after after the string `Report:`. So in the above example the result is expected to be 204.

* Do the same, but only take account lines between the `Begin report` and `End report` section. (sum expected to be 58)



