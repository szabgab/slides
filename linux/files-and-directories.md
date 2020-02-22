# Manipulating Files and Directories
{id: files-and-directories}

## Creating directory
{id: creating-directory}
{i: mkdir}

```
$ mkdir abc
$ mkdir abc/def


$ mkdir x/y/z
mkdir: cannot create directory 'x/y/z': No such file or directory

$ mkdir -p x/y/z
```


## Create a file using 'touch'
{id: touch}
{i: touch}

```
$ touch out.txt
$ ls -l out.txt
-rw-rw-r-- 1 vagrant vagrant 0 Jul 17 10:30 out.txt
```


## Create file using echo
{id: echo-to-file}
{i: echo}

```
echo "Hello World" &gt; out.txt
echo "Hello Again" &gt;&gt; out.txt
```


## Copy files and directories
{id: cp}
{i: cp}

```
cp a.txt b.txt
cp -r x/ y/         will create y and copy all the files of x to y
cp -r x/ y/         will create y/x and copy all the files of x into y/x

cp -i               will ask for confirmation before overwriting files

cp a.txt b.txt      sets current date
cp -p a.txt c.txt   preserves date
```


## Move files or directories
{id: move-files}
{i: mv}

```
$ mv a.txt b.txt
$ mv a.txt b/
$ mv a.txt b.txt c/
$ mv a/ b/

$ mv -i       to prompt before overwriting
```


## Removing File or Directory
{id: removing-directory}
{i: rmdir}
{i: rm}

```
$ rm a.txt           remove file

$ rmdir d/           remove empty(!) directory
$ rm -rf d/          force remove directory tree recursively
```


## Symbolic links
{id: symbolic-links}
{i: ln -s}

* Avialable vs enabled configuration files of Apache or Nginx.
* Backward compatibility: Retain historical location when moving a file or directory.
* Fake directory structure (or location of files).


```
$ ln -s  /tmp
$ ls -l

$ ln -s /etc/passwd
$ ls -l

$ echo "hello" > a.txt
$ ln -s a.txt b.txt 
$ ls -l
```


## Hard links
{id: hard-links}
{i: ln}

```
$ echo "hello" > a.txt
$ ln a.txt b.txt
$ ls -li
```



## Determining File types
{id: file-type}
{i: file}

* By extension?
* Using 'file'



```
$ file /usr/bin/python
/usr/bin/python: symbolic link to `python2.7'
```


```
$ file /usr/bin/python2.7
/usr/bin/python2.7: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV),
dynamically linked (uses shared libs), for GNU/Linux 2.6.32,
BuildID[sha1]=2ca3b615bd7d6141844b6701002b80f148b80d40, stripped
```


```
$ file .viminfo
.viminfo: ASCII text
```


```
$ file a.sh
a.sh: Bourne-Again shell script, ASCII text executable
```


```
$ cp a.sh a
$ file a
a: Bourne-Again shell script, ASCII text executable
```


## Finding files (find)
{id: finding-files}
{i: find}

```
find .

find . -name \*.xml

-name NAME         wilde card for name of the thing
-iname NAME        like name but ignores case
-user  NAME        things owned by the user
-type [fdlcb]      f = file, d = directory, ...
-size [+/-]n[ck]   min or max size
-inum number       inode numbe of the thing (to find hard links)
-mtime [+/-]n      modified time in days.
```


Actions:



```
-exec command {} \;
-ok command {} \;
```

{aside}

A little warning. If we run find . -name *.xml (without escaping the wildcard), the shell will try to expand it in the current working
directory. If it is successful that result will be used as the search term.
{/aside}


## find examples
{id: find-examples}

```
find . -type d
find / -name .profile
find / -type f -size +1k

find / -mtime 10            modified 10 days ago
find / -mtime +10           modified more than 10 days ago
find / -mtime -10           modified less than 10 days ago

find / -mtime -2       = the things found by    -mtime 0   and  -mtime 1
```


exec, ok, and xargs


```
find . -ok echo {} \;
find . -exec echo {} \;
find . | xargs echo
find . -print0 | xargs -0 -I{} echo {}
```


Remove some files


```
find . -name "*.o" -ok rm {} \;
find . /tmp /usr/tmp -name core -exec rm {} \;
```


Rename files without extension to have extension jpg ?


```
find . -type f ! -name '*.*' -exec mv {} {}.jpg \;
find . -type f ! -name '*.*' -print0 | xargs -0 -I{} mv {} {}.jpg
```


## Search indexed files
{id: index-files}
{i: hostname}
{i: hostname}

```
$ locate ...

$ updatedb
```



## Comparing files using diff
{id: diff}
![](examples/linux/a.txt)
![](examples/linux/b.txt)

```
diff a.txt b.txt
2,3c2
&lt; More text
&lt; Third line
---
&gt; Other line
```


## Comparing directories using diff
{id: diff-dirs}

```
diff -r a/ b/
```


## File and Directory Name conventions
{id: name-conventions}

Might depend on the file system.

* Case sensitive.
* Can have spaces.
* Can have Unicode characters.
* Extensions have no special meaning to Linux, but might have special meaning to some applications.
* Usually all lowercase, no spaces, words separated by underscore `_`.


## Exercise: files
{id: exercises-files}

* Create a directory structure under `~/ex/a`  with 3 directories and 5 files
* Copy the whoke structure to `~/ex/b`
* Compare the two using 'diff'
* Add a new file in the `~/ex/a` structure.
* Change the content of one of the files in the `~/ex/b` structure.
* Compare the two directory trees again.


## Exercise: shutdown vs halt
{id: exercise-file-path}

What is the difference between `shutdown`
and `halt`.







