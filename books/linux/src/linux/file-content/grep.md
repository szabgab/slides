# Finding text in a file

* grep
* egrep
* ack-grep

* grep regex FILEs
* egrep regex FILEs
* ack-grep


```
-v lines that did not match
-i ignore case
-n show line numbers
-r look into the files recursively

-w match exact words only
-l print names of the files matched
-c count of lines matched

-B n   show n lines before the match.
-A n   show n lines after the match.
-C n   show n lines both before and after the match (up to 2*n+1 lines) (context).
```

{% embed include file="src/examples/intro/grep.txt" %}


