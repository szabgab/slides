# Scalar references in Getopt::Long

* Getopt::Long



It is used less often than the other references but one of the prominent
uses is the GetOptions function of Getopt::Long.



```perl
use Getopt::Long;
my $file = "default.txt";
my $debug;
GetOptions(
        "file=s" => \$file,
        "debug"  => \$debug,
) or die;
```


