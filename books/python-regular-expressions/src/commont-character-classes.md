# Common characer classes

\d
\w
\s

* **\d** digit: [Unicode Characters in the 'Number, Decimal Digit' Category](https://www.fileformat.info/info/unicode/category/Nd/list.htm) or `[0-9]` if `re.ASCII` is enabled.
* **\w** word character. See the Unicode alphanumeric characters (digits and letters) or `[a-zA-Z0-9_]` (digits, letters, underscore) if `re.ASCII` is enabled.
* **\s** white space: Unicode whitespace characters  or `[\f\t\n\r\v ]` form-feed, tab, newline, carriage return, vertical-tab, and SPACE if `re.ASCII` is enabled.

* Use stand alone: \d or as part of a larger character class: [abc\d]


