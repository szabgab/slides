# System administration basics
{id: sysadmin-basics}

## Basic sysadmin tasks
{id: sysadmin-tasks}

* reboot
* shutdown
* halt
* Package Management - Installing software



## sudo
{id: sudo}
{i: sudo}

```
$ ls -l /root
ls: cannot open directory /root/: Permission denied

$ sudo ls -l /root/
[sudo] password for gabor: 
total 4
drwxr-xr-x 3 root root 4096 Apr 28  2012 SecretRootFile
```


## su
{id: su}
{i: su}

```
$ su -
```


## Logfiles in /var/log
{id: var-log}
{i: /var/log}

```
$ sudo ls -l /var/log
```



## Exercise: sysadmin
{id: exercise-sysadmin}

* List the files in the /root directory
* Reboot the Linux machine from the command line.
* Once it rebooted log in and shut it down from the command line.
* What is the differernce between **ls -l** and **ls -L**. Create an example.





