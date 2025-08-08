# Determining File types

* file

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



