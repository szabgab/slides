# Regex Examples: single character

Any line that has an 'x' in it.

```
Regex: /x/
Input: "abcde"
Input: "abxcde"
Input: "xabcde"
Input: "xabcxde"
```

Any line that starts with an 'x'.

```
Regex: /^x/
Input: "abcde"
Input: "abxcde"
Input: "xabcde"
Input: " xabcde"
Input: "^xabcde"
```


^ at the beginning of the regular expression means, match at the beginning of the string.

