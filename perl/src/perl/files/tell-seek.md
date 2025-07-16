# tell, seek

* tell
* seek


For our purposes a file is a line of characters.
After a bunch of read and/or write operations we need to tell where are we on that line ?


```
LOCATION = tell FILEHANDLE
```

We might also want to move within that file



```
 seek FILEHANDLE, OFFSET, WHENCE
 
 WHENCE:
     0 from beginning of file
     1 from current location
     2 from end of file
 OFFSET: 
     +/- number of bytes to move
```


the important values are:



```perl
seek $fh, 0,0;    # go to the beginning of the file
seek $fh, 0,2;    # go to the end of the file
```



