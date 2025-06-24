# grep

**grep** gets a regex and one or more files. It goes over line-by-line all the files and displays the lines where the regex matched. A few examples:

```
grep python file.xml    # lines that have the string python in them in file.xml.
grep [34] file.xml      # lines that have either 3 or 4 (or both) in file.xml.
grep [34] *.xml         # lines that have either 3 or 4 (or both) in every xml file.
grep [0-9] *.xml        # lines with a digit in them.
egrep '\b[0-9]' *.xml   # only highlight digits that are at the beginning of a number.
```



