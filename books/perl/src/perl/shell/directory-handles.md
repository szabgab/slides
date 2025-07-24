# Directory handles

* opendir
* readdir

For a platform independent approach use opendir and readdir.

In order to read the content of a directory (that is the list of the files)
first we have to open the directory similarly to the way we opened a file
but using the opendir function
This way we get a directory handle which we can use in subsequent operations.

Once the directory was opened successfully we can use the function readdir
in a loop to get the names of the files in that directory

{% embed include file="src/examples/shell/list_directory.pl" %}

in LIST context readdir returns all the files in the directory.

```
opendir(my $dh, "/etc") or die $!;
@files = readdir $dh;
```


