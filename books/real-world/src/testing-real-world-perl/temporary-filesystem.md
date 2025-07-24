# Fake (temporary) filesytem


Use temporary directories and files - locate pathes that are hard-coded in the code and replace them with configuration options from a configuration file or environment variables.
[File::Temp](https://metacpan.org/pod/File::Temp)


```
use File::Temp qw(tempdir);
my $dir = tempdir( CLEANUP => 1 );
```


