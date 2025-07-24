# Substitute

* s/PATTERN/REPLACEMENT/
* s{PATTERN}{REPLACEMENT}


```
$line = "abc123def";

$line =~ s/\d+/ /;       # "abc def"


$line =~ s{
      ([a-z]*)
      (\d*)
      ([a-z]*)
      }
      {$3$2$1}x;        # "def123abc"

```


