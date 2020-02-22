# System information
{id: system-information}

## id
{id: id}
{i: id}

```
$ id
uid=1000(vagrant) gid=1000(vagrant) groups=1000(vagrant)
```


## who
{id: who}
{i: who}

Which user(s) are logged in to the system. Since when. From which IP address.


```
$ who
vagrant  pts/0        2016-07-03 11:12 (10.0.2.2)
```


## w
{id: w}
{i: w}

Which user(s) are logged in to the system. What are they doing?


```
$ w
 19:16:16 up 1 day,  3:17,  2 users,  load average: 0.27, 0.23, 0.17
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
vagrant  pts/1    10.0.2.2:S.0     19:15    1.00s  0.03s  0.00s w
vagrant  pts/2    10.0.2.2:S.1     19:16    9.00s  0.06s  0.03s vim a.txt
```


## whoami
{id: whoami}
{i: whoami}

Print the current user. (same as id -un)


```
$ whoami
vagrant
```


## last
{id: last}
{i: last}

Show listing of last logged in users


```
bar       ttys002                   Wed Jul  6 16:55 - 17:12  (00:16)
foo       ttys002                   Wed Jul  6 13:11 - 13:16  (00:05)
gabor     ttys001                   Mon Jul  4 19:48   still logged in
```


## uname
{id: uname}
{i: uname}

```
uname
Linux
```


```
uname -a
  CPU type - Kernel Architecure - operating system - kernel version
Linux pm 3.11.0-17-generic #31-Ubuntu SMP Mon Feb 3 21:52:43 UTC 2014
  x86_64 x86_64 x86_64 GNU/Linux
```

* CPU type
* Application architecture
* Kernel Architecture




## free
{id: free}
{i: free}

Show free memory.


```
$ free -ht
             total       used       free     shared    buffers     cached
Mem:          3.9G       3.8G        32M        96K        97M       1.1G
-/+ buffers/cache:       2.6G       1.2G
Swap:         1.0G        61M       962M
Total:        4.9G       3.9G       995M
```

* total - physical memory
* cached - memory used to speed up operations. e.g. file read-write operations. This can be used by an application.
* buffers - Temporary memory to help some processes. (e.g. file meta data).
* In the first line  used includes buffers + cached.
* In the second line used only includes memory used by applications.



## vmstat
{id: vmstat}
{i: vmstat}

![](examples/linux/vmstat.txt)


## /proc/meminfo
{id: proc-meminfo}
{i: /proc/meminfo}

![](examples/linux/meminfo.txt)


## Exercise: System information
{id: exercise-system-information}

* Check the free memory on your system right after booting.
* Launch a heavy application that takes a lot of memory in one window.
* Check the free memory again in another window.
* Change the prompt to include the current time in seconds.
* Make the change persistant between terminals and sessions.





