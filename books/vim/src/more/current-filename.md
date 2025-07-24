# Current filename


Copy (yank) the current file (buffer) name to clip-board so you can paste it using p.


```
:let @" = expand("%")
```

Copy the full path:


```
:let @" = expand("%:p")
```



