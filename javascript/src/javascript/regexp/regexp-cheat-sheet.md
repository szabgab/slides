# RegExp cheat sheet

```
var pattern = new RegExp(pattern, modifiers);

. - match any character (except newline)
```


Character classes


* [abcde]  - match a single character: a, b, c, d, or e
* [^abcde]  - match a single character, except of a, b, c, d, and e
* [a-e]  - the same as [abcde]
* \d - a single digit (the same as [0-9])
* \w - a single word characer (the same as [a-zA-Z0-9_]
* \s - a single white space
* \D - a single non-digit (the same as [^\d])



Alternation


* apple|banana



Grouping


()



Quantifiers


* ? - 0 or 1
* + - 1 or more
* * - 0 or more (any number)
* {n, m} - between n and m times (inclusive)



Modifiers


* i - case insensitive
* g - global
* m - multiline



