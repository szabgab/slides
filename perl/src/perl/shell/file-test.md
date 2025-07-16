# File test or -X operators

* -e
* -f
* -d
* -M

```
Before we try to read from a file or try to write to a file
we might want to check our rights, if we can do the required action at all.

For this there is a bunch of so called -X operators. Usually you use them in
an if statement:
```

```
if (-e "file.txt") {
    print "File exists !\n";
}
```

* -e File (or directory) exists
* -r File (or directory) is readable by this user
* -w File (or directory) is writable by this user
* -x File (or directory) is executable by this user
* -f Entry is a file
* -d Entry is a directory
* -l Entry is a symbolic link
* -s Size of the file (hence also means 'file is not empty')
* -M Number of days between the modification date of a file and the start time of our script


```
Hence -s can be used either in an if statement or like this:
```

```
$size = -s $filename;
```

```
There are more such operators see `perldoc -f -x`
```



