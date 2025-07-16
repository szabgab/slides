# Filename creation based on date


```perl
 # creating a filename based on the date YYYY-MM-DD-HH-MM-SS
 @t = (localtime)[5,4,3,2,1,0];
 $t[0]+=1900;
 $t[1]++;
 $filename = sprintf "%d-%0.2d-%0.2d-%0.2d-%0.2d-%0.2d", @t;
```


