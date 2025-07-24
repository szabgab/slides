# Regex Examples (^ in character class)


^ as the first character in a character class means
  "a character that is not listed in this character class"



```
Regex: /#[^abc]#/
Input: "abc #a# z"
Input: "abc #z# z"
Input: "#z#"
Input: "##"
```


