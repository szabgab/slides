# Regex Examples dot .

Any line that has any of the xax, xbx, ...,
that is any character between two x-es.

```
Regex: /x.x/
Input: "abcde"
Input: "abxcxbde"
Input: "xabcde"
Input: "xabxcxde"
Input: "adax xabcde"
Input: "adax.xabcde"
Input: "x.x"
Input: "xx"
```

Only lines that have x.x (A real . between two x-es.)

```
Regex: /x\.x/
```

```
The special characters are: . * + ? ^ $ \ ( ) [ ] | { }    and the delimiter: /

Some of the characters change their special meaning based on position.
```

