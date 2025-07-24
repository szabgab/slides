# Quantifiers on character classes

```
Regex: /-[abc]-/
Input: "-a-"
Input: "-b-"
Input: "-x-"
Input: "-ab-"
```

```
Regex: /-[abc]+-/
Input: "-a-"
Input: "-b-"
Input: "-aa-"
Input: "-ab-"
Input: "-x-"
Input: "--"
```



