# Character classes

A list of optional characters within square brackets []




```
/a[bc]a/      # aba, aca
/a[2#=x?.]a/  # a2a, a#a, a=a, axa, a?a, a.a
              # inside the character class most of the spec characters lose their
              # special meaning  BUT there are some new special characters
/a[2-8]a/     # is the same as /a[2345678]a/
/a[2-]a/      # a2a, a-a        - has no special meaning at the ends
/a[-8]a/      # a8a, a-a
/a[6-C]a/     # a6a, a7a ... aCa
              #      characters from the ASCII table: 6789:;&lt;=&gt;?@ABC
/a[C-6]a/     # syntax error

/a[^xa]a/     # "aba", "aca"  but not "aaa", "axa"    what about "aa" ?
              # ^ as the first character in a character class means
              # a character that is not in the list
/a[a^x]a/     # aaa, a^a, axa
```


