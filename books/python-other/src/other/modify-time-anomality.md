# Modify time anomality

Without calling flush the modify-time of the two files will be the same. Even if we sleep 0.001 seconds.
Despite the fact that the filesystem provide more accurate values.

If we we wait a bit between calls, or if we flush the buffer of the file, then the timestamps will be different.


{% embed include file="src/examples/other/modify_time_is_the_same.py" %}


