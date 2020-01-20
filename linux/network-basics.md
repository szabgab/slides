# Network Basics
{id: network-basics}

## IPv4 vs IPv6
{id: ip}

```
inet addr:10.0.2.15
```


```
inet6 addr: fe80::a00:27ff:fefd:1f04/64
```


## ifconfig
{id: ifconfig}
{i: ifconfig}

```
 ifconfig
eth0      Link encap:Ethernet  HWaddr 08:00:27:fd:1f:04
          inet addr:10.0.2.15  Bcast:10.0.2.255  Mask:255.255.255.0
          inet6 addr: fe80::a00:27ff:fefd:1f04/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:11894 errors:0 dropped:0 overruns:0 frame:0
          TX packets:8887 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:2523362 (2.5 MB)  TX bytes:790877 (790.8 KB)

lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:10183 errors:0 dropped:0 overruns:0 frame:0
          TX packets:10183 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:2904229 (2.9 MB)  TX bytes:2904229 (2.9 MB)

lxcbr0    Link encap:Ethernet  HWaddr 86:d0:36:c7:2e:e8
          inet addr:10.0.3.1  Bcast:0.0.0.0  Mask:255.255.255.0
          inet6 addr: fe80::84d0:36ff:fec7:2ee8/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:7 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:0 (0.0 B)  TX bytes:570 (570.0 B)
```


## Ping
{id: ping}
{i: ping}

```
$ ping google.com
PING google.com (172.217.19.238) 56(84) bytes of data.
64 bytes from s22-in-f14.1e.net (172.217.19.238): icmp_seq=1 ttl=63 time=93.5 ms
64 bytes from s22-in-f14.1e.net (172.217.19.238): icmp_seq=2 ttl=63 time=200 ms
64 bytes from s22-in-f14.1e.net (172.217.19.238): icmp_seq=3 ttl=63 time=84.4 ms
64 bytes from s22-in-f14.1e.net (172.217.19.238): icmp_seq=4 ttl=63 time=95.9 ms
^C
--- google.com ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3009ms
rtt min/avg/max/mdev = 84.425/118.594/200.469/47.466 ms
```



## Traceroute
{id: traceroute}
{i: traceroute}
{i: tracepath}

```
$ tracepath google.com
 1?: [LOCALHOST]                                         pmtu 1500
 1:  10.0.2.2                                              0.571ms
 1:  10.0.2.2                                              0.175ms
 2:  192.168.1.1                                           3.164ms asymm 64
 3:  192.168.0.1                                           1.809ms asymm 63
 4:  bzq-25-85-30.cust.bezeqint.net                       76.260ms asymm 62
 5:  bzq-219-189-245.cablep.bezeqint.net                  22.917ms asymm 61
 6:  bzq-179-124-78.cust.bezeqint.net                     83.441ms asymm 60
 7:  bzq-179-72-241.cust.bezeqint.net                     95.980ms asymm 59
 8:  no replyre
...
```


## /etc/hosts
{id: etc-hosts}

Map names to IP addresses locally. Override DNS.




## Telnet
{id: telnet}
{i: telnet}


## ssh - Secure Shell
{id: ssh}
{i: ssh}

```
$ ssh hostname
$ ssh user@hostname
$ ssh -p port hostname

$ ssh hostname "command; command; ...."
```


## Public key access
{id: public-key-access}

```
$ ssh foo@localhost
...
foo@localhost's password:
```

Look at ~/.ssh


```
ls -l ~/.ssh
    authorized_keys
    known_hosts
```


## Generate public key
{id: ssh-keygen}
{i: ssh-keygen}

```
$ ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/vagrant/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/vagrant/.ssh/id_rsa.
Your public key has been saved in /home/vagrant/.ssh/id_rsa.pub.
The key fingerprint is:
bd:67:29:a2:92:db:7f:70:4b:00:8b:d0:36:2e:19:5a vagrant@perl-maven
The key's randomart image is:
+---[RSA 2048]----+
|                 |
|                 |
|                 |
|         .       |
|o E o +    . .   |
|+ o +.o. . +     |
| .  .ooo.        |
+-----------------+
```

```
.ssh/id_rsa
.ssh/id_rsa.pub
```


## Add public key
{id: add-public}

```
$ scp .ssh/id_rsa.pub foo@localhost:

$ ssh foo@localhost

# if .ssh does not exist yet:

$ mkdir .ssh
$ ls -ld .ssh
drwxrwxr-x 2 foo foo 4096 Jul 17 05:51 .ssh/
$ chmod 0700 .ssh/


$ cat id_rsa.pub >> .ssh/authorized_keys
$ rm id_rsa.pub
```



## ftp - File Transfer Protocol
{id: ftp}
{i: ftp}


## scp - Secure Copy
{id: scp}
{i: scp}

```
$ scp localfile user@remote:/path/to/
$ scp -r  localdir/   user@remote:/dir
```


## rsync
{id: rsync}
{i: rsync}

```
rsync source hostname:destination

 --archive
 --verbose
 --recursive
 --progress N
 --delete-after
 --rsh="ssh -p port -l user"
```


## curl and wget to fetch web pages
{id: curl}
{i: curl}
{i: wget}

```
$ curl http://google.com/
$ wget http://google.com/
$ cat index.html
```


## Command line browsers
{id: command-line-browsers}

* lynx
* w3m
* elinks



## Sending mail from the command line
{id: mail}

* mail
* mail foo@bar.com &lt; file




## Keep remote session using screen
{id: screen}
{i: screen}

```
$ ssh remote
$ screen
  ... do stuff ...
  get disconnected

$ ssh remote
$ screen -dr
  ... back where you were ...
```


* screen         - to start a new session.
* screen -dr     - to attach to an existing session.
* Ctrl-a Ctrl-d  - to detach from an existing session.



* Ctrl-a Ctrl-c    Create new Window
* Ctrl-a w         List Windows
* Ctrl-a 0         Jump to Window 0
* Ctrl-a ?         Help
* Ctrl-d           Close current window (close screen)



## Keep remote session using tmux
{id: tmux}
{i: tmux}

* tmux       - launch a new session
* tmux ls    - list sessions
* Ctrl-b s   - list sessions
* Ctrl-b d   - detach from current session.
* tmux a     - attache to running session.
* Ctrl-b ?   - list of key bindings



## tmux multiple session
{id: tmux-multiple-session}

```
$tmux                    - create new session (name 0)
$ echo "session 0"
$ Ctrl-b d               - detach

$ tmux                   - create new session (name 1)
$ echo "session 1"
$ Ctrl-b d               - detach

$ tmux new -s sample     - new session (name sample)
$ echo sample
$ Ctrl-b d               - detach

$ tmux ls
0: 1 windows (created Wed Jul 20 11:51:58 2016) [101x50]
1: 1 windows (created Wed Jul 20 11:52:02 2016) [101x50]
sample: 1 windows (created Wed Jul 20 11:54:53 2016) [101x50]

$ tmux a -t 1            - attach to session 1
$ Ctrl-b d
$ tmux a -t sample       - attach to session sample

$ Ctrl-b s               - list sessions and select another one
$ Ctrl-b $               - rename current session

$ tmux kill-session -t session-name     - or just exit the window with Ctrl-d
```


## iftop
{id: iftop}
{i: iftop}

```
$ sudo iftop
```

* Right hand side: average traffic in the last 2, 10, 40 seconds
* h - to get help
* p - to show ports
* n - toggle DNS host resolution
* L - liner/logarithmic scale
* s - show/hide source IP
* S - show/hide source port
* d - show/hide destination IP
* D - show/hide destination port



## Port used by (lsof - list open files)
{id: port-used-by}
{i: lsof -i N}

```
$ sudo lsof -i :22     list the process using port 22
```


## Port used by example 2
{id: port-used-by-2}
{i: nc}

```
$ nc -l localhost 10000 > log.txt
$ telnet localhost 10000
$ sudo lsof -i :10000

$ sudo cat /proc/PID/cmdline
```


## Network ports
{id: network-ports}

How to identify used and free ports?


```
$ sudo lsof -i         list all the processes using some port

/proc/PID/exe          is a symlink to the real executable
/proc/PID/cmdline      is the content of the command line
/proc/PID/cwd          current working directory of the process
```



## Show ports used with netstat
{id: netstat}
{i: netstat}

```
$ sudo netstat -tulpn
```

* sudo - regular user won't see everything
* -t show tcp
* -u show udp
* -l show only listening sockets
* -p show both PID and the name of the program
* -n show numberic IP and port



## Routing configuration
{id: route}
{i: route}
{i: netstat}

```
$ netstat -nr
Kernel IP routing table
Destination     Gateway         Genmask         Flags   MSS Window  irtt Iface
0.0.0.0         10.0.2.2        0.0.0.0         UG        0 0          0 eth0
10.0.2.0        0.0.0.0         255.255.255.0   U         0 0          0 eth0
10.0.3.0        0.0.0.0         255.255.255.0   U         0 0          0 lxcbr0
```


```
$ route
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
default         10.0.2.2        0.0.0.0         UG    0      0        0 eth0
10.0.2.0        *               255.255.255.0   U     0      0        0 eth0
10.0.3.0        *               255.255.255.0   U     0      0        0 lxcbr0
```



## write
{id: write}
{i: write}
{i: Ctrl-D}

Send messages to other users on the system by typing


```
$ write username
type your message
here
Ctrl-D
```


## Chat with users using ytalk
{id: chat-with-users-ytalk}

```
$ who
$ ytalk user#tty
```

Will split the window to 2 parts to talk to each other.




## Exercise: Networking
{id: exercise-networking}

* Try pinging and tracerouting some other servers. Including code-maven.com
* Try to access some of the servers in your own company using ping/traceroute/telnet/ssh
* Download the main web page of your company and look at its source.
* Fetch the headers the web site returns. (Read about it in the man of curl.)



## Exercise: lorem ipsum
{id: exercise-lorem-ipsum}

* Download the main page of lorem ipsum
* How many lines are there in total?
* How many lines contain the word "lorem" ?
* How many lines in the first half of the page have the word "lorem"?





