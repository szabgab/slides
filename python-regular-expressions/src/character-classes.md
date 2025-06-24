# Character classes

[]
-


We would like to match any string that has any of the #a#, #b#, #c#, #d#, #e#, #f#, #@# or #.#


{% embed include file="src/examples/regex/character_class.py" %}

```
r'#[abcdef@.]#'
r'#[a-f@.]#'
```


