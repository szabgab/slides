# Remove spaces regex

This is not necessary as we can use rstrip, lstrip, and replace.


{% embed include file="src/examples/regex/remove_spaces_regex.py" %}


both ends:



```
re.sub(r'\s*(.*)\s*$', r'\1', line)  #  " abc " =>  "abc "  because of the greediness
```


```
re.sub('^\s*(.*?)\s*$', '\1', line)  #   " abc " =>  "abc"  minimal match
```


