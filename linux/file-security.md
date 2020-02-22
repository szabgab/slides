# File security - File system rights management
{id: file-security}

## ls -l
{id: ls-l}
{i: ls -l}

```
drwxrwxr-x  8 vagrant vagrant 4096 Mar  7 20:08 Abc
-rwxrwxr-x  1 vagrant vagrant  476 Jun  6 15:39 a.sh
lrwxrwxrwx  1 vagrant vagrant    4 Jul  3 15:39 b -> a.sh
```

* 1 char  for type
* 3 chars for user (u)
* 3 chars for group members (g)
* 3 chars for others (o)


Type


```
- is file
d is directory
l is symbolic link
```

Rights


```
r - Read
w - Write
x - eXecute
```


## chmod
{id: chmod-characters}
{i: chmod}

```
$ touch some_file
$ ls -l some_file
-rw-rw-r-- 1 vagrant vagrant 0 Jul  7 14:58 some_file

$ chmod 0 some_file
---------- 1 vagrant vagrant 0 Jul  7 14:58 some_file

$ chmod u+rw some_file
-rw------- 1 vagrant vagrant 0 Jul  7 14:58 some_file

$ chmod a+x some_file
-rwx--x--x 1 vagrant vagrant 0 Jul  7 14:58 some_file

$ chmod o-x some_file
-rwx--x--- 1 vagrant vagrant 0 Jul  7 14:58 some_file
```


## chmod octal
{id: chmod-octal}

```
$ chmod 0753 some_file
-rwxr-x-wx 1 vagrant vagrant 0 Jul  7 14:58 some_file
```


```
4  - r
2  - w
1  - x

     rwx
7  = 111
5  = 101
3  = 011
```


## Change ownership with chown
{id: chown}
{i: chown}

```
$ chown foo.marketing file.txt

$ chown foo:marketing file.txt
```


## Change group only using chgrp
{id: chgrp}
{i: chgrp}

Change the group of a file or a directory.


```
$ chgrp marketing file.txt
```


## Default file permissions: umask
{id: umask}
{i: umask}

By default files would be created with permission 0666 which means rw for everyone.


**umask** helps having more secure defaults.


The bits that are set in umask won't be set by the applications.
So if we have umask 0777 then every file will be created without any rights.
If the umask is 0000 then it has no effect and files will be created with 0666.


```
$ umask    to show the current value
$ touch file1
$ ls -l file1

$ umask 0022
$ touch file2
$ ls -l file2
```



## Shell Script
{id: shell-script}
{i: sh-bang}
{i: chmod +x}

![](examples/linux/hello_world.sh)

```
$ chmod u+x hello_world.sh
$ ./hello_world.sh
```


## Perl
{id: perl}

![](examples/linux/hello_world.pl)

```
$ perl hello_world.pl
$ chmod u+x hello_world.pl
$ ./hello_world.pl
```


## Python
{id: python}

![](examples/linux/hello_world.py)

```
$ python hello_world.py
$ chmod u+x hello_world.py
$ ./hello_world.py
```


## Exercise: Create Bash script
{id: exercise-create-bash-script}

* Create a shell script that will print "Hello Linux".
* Try to run it.
* Make it executable and try to run it again.



## Exercise: File security
{id: exercise-file-security}

* Create a file.
* Change its rights.
* Change its owner.
* ...



## Exercise: Remove write protected file
{id: exercise-remove-write-protected-file}

1. Create a file that has no rights at all. Try to remove it.



1. Create a directory and in it create a file that has no rights.
1. Remove the write rights from the directory.
1. Try to remove the file.



1. Create a directory and in it create a file.
1. Remove the eXecutable bit from the directory.
1. Try to list the content of the directory.



## Exercise: chmod
{id: exercise-chmod}

* Create a file and set the permissions to -r--r--r--
* Then set it to -rwx-------



* Create a second user.
* Create a file by your regular user and make sure the other user cannot see the content.
* Create another file that the user can read but cannot write.
* Create a Hello World shell script. Make sure both of you can run it but only you can write it.
* Create a 3rd user. Make sure only the first 2 users can execute the script.



## Solution: chmod
{id: solution-chmod}

* Create a second user **sudo adduser foo**
* Create the file and make it  executable by owner and by group **chmod ug+x hello.sh**
* Create a new group:   **sudo groupadd exe**
* Add my user (vagrant) to this group: **sudo usermod -a -G exe vagrant**
* Add the second user (foo) to the group: **sudo usermod -a -G exe foo**
* Change the group of the file to be the new common group: **sudo chgrp exe hello.sh**






