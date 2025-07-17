# One-liner: Change encoding

* -i
* -M
* -p
* Encode


Convert all the .srt files that are Windows Hebrew encoded to UTF-8 keeping a backup copy
of the original file with a .bak extension.

```
-i    - inplace editing
.bak  - generate backup with that extension
-M    - load  module as 'use' would do
-p    - go over line by line on the file, put the line in $_, execute the
        command on it and then print the result.
        In case of inplace editing, save it back to the file.
```

```
perl -i.bak -MEncode -p -e "Encode::from_to($_, 'Windows-1255', 'utf-8')" video.srt
```

{% embed include file="src/examples/oneliners/encode_files.pl" %}


