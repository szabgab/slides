# Exercise: parse file

In the following file we have lines:

```
SOURCE/FILENAME.json,TARGET
```

read in the file and create

* a single dictionary where the `SOURCE/FILENAME.json` is the key and the TARGET is the value.
* list of dictionaries in which the keys are 'source', 'filename', and 'target' and the values are from the respective columns (SOURCE, FILENAME.json, and TARGET)

You can solve this `for`-loop or with `map` and list-comprehensions. Do it in both ways.

{% embed include file="src/examples/functional/books.txt)



