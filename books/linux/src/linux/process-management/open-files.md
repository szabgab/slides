# List open files (lsof)

* lsof

In one window run this perl script as user 'foo': **perl examples/linux/open_file.pl README**. In another window


```
$ lsof | head -1                          (to print the header)
$ sudo lsof | grep README                 (to print the line with the details)
COMMAND   PID   TID USER  FD   TYPE DEVICE SIZE/OFF   NODE NAME
perl    32242        foo   3r   REG   0,41      5950  61972 /vagrant/training/linux/README

$ sudo ls -l /proc/32242
$ sudo less /proc/32242/cmdline
```



