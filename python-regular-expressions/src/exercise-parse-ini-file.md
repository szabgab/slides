# Exercise: Parse ini file

An ini file has sections starting by the name of the section in square brackets and within
each section there are key = value pairs with optional spaces around the "=" sign.
The keys can only contain letters, numbers, underscore or dash.
In addition there can be empty lines and lines starting with # which are comments.

Given a filename, generate a 2 dimensional hash and then print it out.
Example ini file:

{% embed include file="src/examples/regex/inifile.ini)

If you print it, it should look like this (except of the nice formatting).

{% embed include file="src/examples/regex/inifile.out" %}



