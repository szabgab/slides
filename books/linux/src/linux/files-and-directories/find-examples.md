# find examples

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


