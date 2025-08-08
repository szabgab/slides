# du -s

```
$ du -hs *          (human-readable, summarize)
4.0K    README
1.1M    build
212K    examples
 24K    intro.xml
4.0K    linux.yml
 16K    scripts.xml
4.0K    variables.xml
```


```
$ du -s * | sort -n -r
2288    build
424     examples
48      intro.xml
32      scripts.xml
8       variables.xml
8       linux.yml
8       README
```



