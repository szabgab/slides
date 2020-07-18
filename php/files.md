# PHP - Files
{id: php-files}

## Read from file
{id: read-from-file}
{i: fopen}
{i: fgets}

{aside}

Use **fopen** with the parameter **r** to open a file for reading and then use **fgets** to read the content line-by-line.
Use **fclose** to close the filehandle.
PHP closes the file at the end of the program but it is better practice to close it by ourself.
{/aside}
![](examples/files/readfile.php)


## Fail to open file
{id: open-fails}
![](examples/files/open_fails.php)

```
Warning: fopen(no_such_dir/text.txt): failed to open stream:
   No such file or directory in .../php/examples/files/open_fails.php on line 2
Still running
```


## Checking if open file succeded
{id: open-fails-checking}
![](examples/files/open_fails_checked.php)

```
Warning: fopen(no_such_dir/text.txt): failed to open stream:
   No such file or directory in .../php/examples/files/open_fails.php on line 2
Still running
data/text.txt succeeded
```


## Checking if open file succeded - suppress warnigs
{id: open-fails-checking-suppress-warnings}
{i: @}
![](examples/files/open_fails_checked_nowarn.php)

```
Still running
data/text.txt succeeded
```


## Read CSV file
{id: read-csv-file}
{i: fgetcsv}

{aside}

**fgetcsv** returns an array of the values.
{/aside}
![](examples/files/readcsv.php)


## Open file to read or write
{id: open-file-to-read-or-write}

* $fh = fopen("file", r);
* Other flags are "w", "r+", "w+", "a", "a+", "x" (create if not exists), "x+" (... also read)



## Write to a file
{id: write-to-a-file}
{i: fwrite}
![](examples/files/writefile.php)


## Fail to write to a file
{id: write-to-file-failed}
![](examples/files/writefile_fail.php)


## Registration form - save to fill
{id: registration-form}
![](examples/files/register.php)


## copy - Copy a file
{id: copy}
{i: copy}
![](examples/files/copy.php)


## unlink - Delete a file
{id: unlink}
{i: unlink}
![](examples/files/unlink.php)


## chmod
{id: chmod}
{i: chmod}
![](examples/files/chmod.php)


## chown - Change owner
{id: chown}
{i: chown}
![](examples/files/chown.php)



## Get current working directory - getcwd
{id: getcwd}
![](examples/files/getcwd.php)


## Show source
{id: show-source}
{i: file_get_contents}
{i: htmlspecialchars}
![](examples/files/show_source.php)




