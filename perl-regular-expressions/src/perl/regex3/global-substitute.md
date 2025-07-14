# Global substitute

```
$line = "abc123def";

$line =~ s/.../x/;           # "x123def";

$line =~ s/.../x/g;          # "xxx";


$line =~ s/(.)(.)/$2$1/;     # "bac123def"

$line =~ s/(.)(.)/$2$1/g;    # "ba1c32edf"
```


