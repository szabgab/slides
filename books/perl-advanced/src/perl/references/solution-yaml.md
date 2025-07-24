# Solution: save ini and csv as YAML

Just add the following code:

```perl
use YAML qw(DumFile);
DumpFile 'ini.yml', \@data; # in read_csv_file_hash.pl

DumpFile 'ini.yml', \%ini; # in read_ini_file.pl

DumpFile 'csv.yml', \%data; # in read_csv_file_hash.pl
```


