# Process and Job Management
{id: process-management}

## uptime
{id: uptime}
{i: uptime}

```
$ uptime
11:04:46 up 13:25,  1 user,  load average: 0.13, 0.17, 0.15
```


## ps
{id: ps}
{i: ps}
{i: pstree}

```
$ ps         (PID, TTY, TIME, CMD)
$ ps -f      full format (UID, PPID, STIME)
$ pe -e      All processes

$ pstree
$ pstree -p       Show the IDs as well
```


## System load: top
{id: system-load-top}
{i: top}

* top



## System load: htop
{id: system-load-htop}
{i: htop}

* Tree view / List view
* u - user
* F - follow



## Process state
{id: process-state}

* R - Running or runnable
* S - Sleep - waiting for event to complete
* T - Stopped (Ctrl-Z) or traced
* D - Uninterruptable sleep (IO)
* Z - Zombie (defunct) terminated but not reaped



## Process control
{id: process-control}
{i: kill}

```
$ kill       SIGTERM   (same as kill -15)  = please die
$ kill -9    SIGIKILL                      = die now!
$ kill -l    list available signals

$ man 7 signal
```



## Job control
{id: job-control}
{i: jobs}
{i: fg}
{i: bg}
{i: Ctrl-C}
{i: Ctrl-Z}

"**jobs**" are processes related to the current shell.


* Run this **command**: **(while [ 1 ]; do (date; sleep 1); done)**
* suspend job: Ctrl-Z     SIGTSTP   (same as kill -20)  = stop for now
* **bg [job]** will move the specific (or current) job to the background.
* **fg [job]** will move the specific (or current) job to the foreground.

* **command &amp;** run in the background.

* **jobs** will show all the background jobs
* %number - reference to a job number
* %string - job whose name begins with string
* %?string - job whose name contains string
* %+ or %% - current job
* %- - previous job
* Ctrl-C     SIGINT    (same as kill -2)   = please die
* **kill [-signal] job** will send a signal to the given process.



## Refuse to die
{id: refuse-to-die}

![](examples/linux/refuse_to_die.pl)

* Run the above program
* Press **Ctrl-C**
* from another window run **kill PID**
* from another window run **kill -15 PID**
* from another window run **kill -2 PID**
* from another window run **kill -9 PID**
* Run it again
* **Ctrl-Z**
* **kill -20 POD**



## killall
{id: killall}
{i: killall}

**killall NAME** Kill all the process by the given name


```
$ perl -e 'sleep 1 while 1' &amp;
$ perl -e 'sleep 1 while 1' &amp;
$ perl -e 'sleep 1 while 1' &amp;
$ ps -ef | grep perl
$ killall perl
$ ps -ef | grep perl
```



## Zombie demonstration
{id: zombie-demonstration}

In one window launch htop and filter to 'perl'. In another window run this script.

![](examples/linux/create_zombie.pl)


## Reaping child processes demonstration
{id: reaping-child-process-demonstration}
![](examples/linux/reap_child_process.pl)


## Stopped process demonstration
{id: stopped-process-demonstration}

* In one window run **htop** and filter to 'perl'.
* In the second window run  **perl -e '&lt;STDIN&gt;'**
* Look at the htop display to see the process appearing with a state S
* Press **Ctrl-z** in the window with the process.
* Look at the htop display to see the process appearing with a state T
* **bg** will move the process to the background but the state will stay in T.
* **fg** will move it to the foreground and the state will change to S.
* **ENTER** will finish the process.
* Do the same with this example: **perl -e 'sleep 1 while 1'**
* In this case moving to the background will already move the process to S state.



## List open files (lsof)
{id: open-files}
{i: lsof}

In one window run this perl script as user 'foo': **perl examples/linux/open_file.pl README**. In another window


```
$ lsof | head -1                          (to print the header)
$ sudo lsof | grep README                 (to print the line with the details)
COMMAND   PID   TID USER  FD   TYPE DEVICE SIZE/OFF   NODE NAME
perl    32242        foo   3r   REG   0,41      5950  61972 /vagrant/training/linux/README

$ sudo ls -l /proc/32242
$ sudo less /proc/32242/cmdline
```


## Current working directory of a process
{id: pwdx}

```
$ sudo pwdx PID
```


## Services
{id: services}
{i: service}

```
$ sudo service stop
$ sudo service start
$ sudo service restart
$ sudo service reload
```


## tail multiple log files
{id: tail-multiple-log-files}

```
$ (while [ 1 ]; do (echo -n "one "; date; sleep 1); done) &gt; one.txt &amp;
$ (while [ 1 ]; do (echo -n "two "; date; sleep 1); done) &gt; two.txt &amp;

$ tail -f one.txt -f two.txt
$ multitail one.txt two.txt
```



