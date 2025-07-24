# IO (files)

```
open my $fh, '<', $filename or die "Could not open '$filename' for reading $!";

open my $fh, '>', $filename or die "Could not open '$filename' for writing $!";

open my $fh, '>>', $filename or die "Could not open '$filename' to append $!";

my $line = <$fh>;   # Read a line from a text file
```


