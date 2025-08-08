# Symbolic links

* ln -s

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



