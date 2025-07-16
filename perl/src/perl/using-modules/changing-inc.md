# Changing @INC


Set the environment variable
PERL5LIB or PERLLIB for all the scripts



```
export PERL5LIB=/path/to/lib
```


Adding a path to the beginning of @INC. Good for the specific script



```
BEGIN {
   unshift @INC, '/path/to/lib';
}
```


The same but with the standard tool:



```
use lib '/path/to/lib';           # good for the specific script
```


On the command line. Good for this invocation only.



```
perl -I /path/to/lib script.pl
```

[How to change @INC to find Perl modules in non-standard locations](https://perlmaven.com/how-to-change-inc-to-find-perl-modules-in-non-standard-locations)



