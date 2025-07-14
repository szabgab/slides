# Regex Examples (character class)

Any line that has any of the #a#, #b#, #c#, #d#, #e#, #f#, #@# or #.#

```
Regex: /#[abcdef@.]#/
Input: "ab #q# "
Input: "ab #z#a# "
Input: "ab #.# "
Input: "ab ## "
Input: "#a#"
Input: "##"
Input: "###"
```

```
Regex: /#[a-f@.]#/
```


