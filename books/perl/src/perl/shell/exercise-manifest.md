# Exercise: MANIFEST file

We have a file called MANIFEST listing all the required files in a distribution. One file on every line.

Check if all the file exist.

Check if there are files that are not listed in MANIFEST

Optionally allow for wildcards in the file ?

Example MANIFEST file:

{% embed include file="src/examples/shell/package/MANIFEST" %}


Expected solution:

```
File 'Makefile.PL' listed in MANIFEST is missing from package
File 'CHANGES' on disk but is not listed in MANIFEST
```




