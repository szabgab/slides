# Incorrect use of conditions


In your normal speech you could probably say something like "If status_code is 401 or 302, do something.".
Meaning status_cone can be either 401 or 302.

If you tried to translate this into code directly you would write something like this:


```
if status_code == 401 or 302:
    pass
```

Python treats it as if we wrote:

```
if (status_code == 401) or 302:
    pass
```



However, this is incorrect. This condition will always be true  as this is actually same as if you wrote: 
`if (status_code == 401) or (302)` so it will compare status_code to 401, and it will separately check if
302 is True, but any number different from 0 is considered to be True so the above expression will always be True.


What you probably meant is this:

```
if status_code == 401 or status_code == 302:
    pass
```

Alternative way:


An alternative way to achieve the same results would be though probably at this point we have not learned the "in"
operator, nor lists (comma separated values in square brackets):


```
if status_code in [401, 302]:
    pass
```


