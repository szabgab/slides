# One-liner: Replace a string in many files

* -i
* -p

You have a bunch of text files in your directory mentioning the name:

"Microsoft Word"

You are told to replace that by

"OpenOffice Write"

```
perl -i -p -e "s/Microsoft Word/OpenOffice Write/g" *.txt
```

```
-i = inplace editing
-p = loop over lines and print each line (after processing)
-e = command line script
```


