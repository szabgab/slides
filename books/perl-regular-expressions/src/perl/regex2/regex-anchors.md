# Anchors

* anchors
* ^
* $
* \b

```
^            # at the beginning of the pattern means beginning of the string
$            # at the end of the pattern means the end of the string

/the/        # matches anywhere in the string:
             # "atheneum", "thermostat", "the", "mathe"

/^the/       # matches only if the string starts with the
             # "thermostat", "the"

/the$/       # matches only if the string ends with the
             # "the", "mathe"

/^the$/      # matches only if the string
             # "the"

/^The.*finished$/
             # starts with  "The" ends with "finished" and anything in between


\b           # Word delimiter
/\bstruct\b/ # match every place the word "struct" but not
             # "structure" or "construct"
```


