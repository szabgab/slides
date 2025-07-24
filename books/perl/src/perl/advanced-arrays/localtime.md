# The year 19100


First, let's talk about time.


* time}
* localtime}
* gmtime}

```
$t = time();         # 1021924103
                     # returns a 10 digit long number,
                     # the number of seconds since 00:00:00 UTC, January 1, 1970

$x = localtime($t);  # returns a string like           Thu Feb 30 14:15:53 1998
$z = localtime();    # returns the string for the current time

$z = localtime(time - 60*60*24*365);
   # returns the string for a year ago, same time, well almost

@y = localtime($t);  # an array of time values:
                     # 53 15 14 30 1 98 4 61 0
                     # the 9 values are the following:

#  0    1    2     3     4    5     6     7     8    (the index)
($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);

# The localtime function is aware of what is on the left side of the = sign !!!!
```


```
# OK but where does that 19100 come from ?
$mon  0..11
$min  0..59
$sec  0..60
$year YEAR-1900         # for example 2000-1900 = 100
                        # but people used  "19$year"   instead of 1900 + $year
                        # which is          19100      instead of 2000
```


gmtime is the same just gives the time as it is in Greenwich.
[The year of 19100](https://perlmaven.com/the-year-19100)



