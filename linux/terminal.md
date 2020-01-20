# Terminal
{id: terminal}

## The powers of the shell
{id: the-powers-of-the-shell}

* TAB completition
* Command history
* Command chaining (redirection, pipe)
* Wildcards (Meta Characters, globbing)


* Aliases.
* Scripting - Programmability.
* Flexibility.
* Using all ten fingers.



## TAB completition
{id: tab-completition}

```
$ ls /...
$ apt-get install pyth...
```


## Command History
{id: history}

* Up and Down arrows
* history



## Chaining commands: Quick Apache/Nginx log analyzer
{id: quick-apache-nginx-log-analyzer}

```
cut -f1 -d ' ' examples/apache_access.log | sort | uniq -c | sort -k1 -n | tail -1
```

* Take the Apache access log.
* Get the first field of every line where the fields are separated by spaces.  (These are the IP addresses of the visitors.)
* Sort them.
* Drop duplicates prefixing each value by the number of occurances.
* Sort the new double column by the numeric value of the first field.



## Remove temp files
{id: remove-temp-files}

```
ls -l /tmp/ | grep "Jul  3" | cut -d ' ' -f 22 | xargs -I{} ls -ld /tmp/{} | less
ls -l /tmp/ | grep "Jul  3" | cut -d ' ' -f 22 | xargs -I{} rm -rf /tmp/{}

```

* List all the things in the /tmp directory
* Filter those that were created on "Jul  3".
* Limit the output to the filenames only.
* Execute rm -rf on all of them.





## Shells
{id: shells}
{i: csh}
{i: tcsh}
{i: ksh}
{i: sh}
{i: bash}
{i: zsh}

* [C Shell (csh)](https://en.wikipedia.org/wiki/C_shell)
* [TENEX C Shell (tcsh)](http://en.wikipedia.org/wiki/Tcsh)
* [Korn Shell (ksh)](https://en.wikipedia.org/wiki/Korn_shell)
* [Bourne Shell (sh)](https://en.wikipedia.org/wiki/Bourne_shell)
* [Bourne Again Shell (bash)](https://en.wikipedia.org/wiki/Bash_(Unix_shell))
* [Z Shell (zsh)](https://en.wikipedia.org/wiki/Z_shell)



## echo
{id: echo}
{i: echo}
{i: -n}

{aside}

**echo** prints its parameters to the screen (standard output) follwed by a newline.
-n supresses the additional newline. (Mostly interesting for scripts).
{/aside}

```
echo hello world
echo "hello world"
echo -n "hello world"
```



## Actions on ENTER
{id: actions-on-enter}

* Meta-character expansion.
* Variable substitution.
* Splitting of commands.
* Setup redirection.
* Command execution



## Actions on ENTER - examples
{id: actions-on-enter-examples}

* Meta-character expansion. **echo ***
* Variable substitution. **echo "Hello $USER"**
* Splitting of commands. **echo "Hello"; echo "World"**
* Setup redirection. **echo "Hello"; echo "World" &gt; /dev/null**
* Command execution



## Meta-characters (Wildcards)
{id: meta-characters}
{i: ?}
{i: *}
{i: []}
{i: {}}

* ? match any single character
* * match any number of characters (0 or more) (except /)
* [abC] character class - matches a, b, or C
* [b-e] character class - matches b, c, d, or e
* [!b-e] character class - matches any single character except b, c, d, or e
* name_{x,y,z} - name_x, name_y, name_z all at the same time


{aside}

Can be used with 'ls' and other commands on the command line.
{/aside}



## Information about the shell
{id: info-about-the-shell}
{i: $HOME}
{i: $0}
{i: $BASH_VERSION}
{i: $version}
{i: $SHELL}

```
echo $HOME
echo $0              Current shell.
echo $BASH_VERSION
echo $version        In csh like shells such as tcsh.
echo $SHELL          The default shell of the user.
```


## Change password using passwd
{id: change-password}
{i: passwd}

```
$ passwd
Old Password:
New Password:
Retype Password:
```


## Getting Help
{id: help}
{i: -h}
{i: --help}

```
$ passwd -h          # get some help
$ passwd --help      # get some help

$ ls -h              # show how sizes are d
$ ls --help          # some help

$ echo -h            # just prints -h
$ echo --help        # just prints --help
```



## Documentation: man
{id: man}
{i: man}

* man
* man passwd
* man ls
* man echo
* man man
* man -h


Keyboard


```
space  - next page
enter  - next line
b      - prev page
q      - quit
h      - help
q      - quit from the help
1G     - jump to the first line

/      - search
n      - next hit
N      - previos hit
```


## whatis and man sections
{id: whatis}
{i: whatis}

```
$ whatis passwd
passwd (1)           - change user password
passwd (1ssl)        - compute password hashes
passwd (5)           - the password file

$ man 5 passwd
$ man 1ssl passwd
```


## Apropos
{id: apropos}
{i: apropos}

**man -k**


```
$ apropos passwd
chgpasswd (8)        - update group passwords in batch mode
chpasswd (8)         - update passwords in batch mode
Crypt::SmbHash (3pm) - Perl-only implementation of lanman ...
fgetpwent_r (3)      - get passwd file entry reentrantly
getpwent_r (3)       - get passwd file entry reentrantly
gpasswd (1)          - administer /etc/group and /etc/gshadow
grub-mkpasswd-pbkdf2 (1) - generate hashed password for GRUB
htpasswd (1)         - Manage user files for basic authentication
pam_localuser (8)    - require users to be listed in /etc/passwd
passwd (1)           - change user password
passwd (1ssl)        - compute password hashes
passwd (5)           - the password file
passwd2des (3)       - RFS password encryption
SSL_CTX_set_default_passwd_cb (3ssl) - set passwd callback for encrypted PEM file handling
SSL_CTX_set_default_passwd_cb_userdata (3ssl) - set passwd callback for encrypted PEM file handling
update-passwd (8)    - safely update /etc/passwd, /etc/shadow and /etc/group
```



## Sections of the man pages
{id: man-sections}

See also **man man**


1. User command (Programs)
1. system calls
1. Library calls
1. Special files (devices)
1. File formats and configuration files
1. Games
1. Overview, conventions, and miscellaneous
1. System management commands



## Command history
{id: command-history}
{i: history}
{i: HISTFILE}
{i: !}
{i: Ctrl-r}

{aside}

Commands executed in the shell are saved in a file. By default in **~/.bash_history**
but the filename is controllable by the **HISTFILE** environment variable.
HISTFILESIZE can be used to configure the number of lines saved in that file.
HISTSIZE can be used to control the number if lines save in the memory during a session (before saving it to the file)
The actual file is written when the shell exits. If there are multiple shells open, each will have its own history in memory
and each will write it to the file, the second exiting will overwrite the file written by the first one.
Use the **history** command to list the content of history buffer. Use ! N to run command N, or ! -N  or ! name.
{/aside}

* Up/Down arrows
* history
* !!    - the last comand
* ! N   - command number N
* Ctrl-r  -  reverse-i-search
* man bash   to see even more options.



## which and !!
{id: which-and-history}

```
$ which adduser
$ ll `!!`
```


## List all commands in history
{id: list-commands}

List all the commands in the shell history and show them in abc order.


```
$ history | cut -c 8- | sort | less
```


## Clear screen
{id: clear-screen}
{i: clear}
{i: Ctrl-l}

* clear
* Ctrl-l



## Virtualbox: Network access resources
{id: virtual-box-network-access-resources}

* [SSH between Mac OS X host and Virtual Box guest ](https://gist.github.com/wacko/5577187)
* [VirtualBox: How to access guest (CentOS) webserver from the host (Mac OS X) on NAT](https://aruljohn.com/info/virtualbox-access-guest-from-host-nat/)



## Virtualbox: Allow access from Host to Guest
{id: virtual-box-network-access}

* Virtual Box / Preferences / Network / Host only network
* + to add one (vboxnet0)
* Select your VirtualBox / Setup / Network
* Adapter 1 is set to NAT.
* Click to Adapter 2
* Set it to "Host only" and selectec the vboxnet0



## Virtualbox: Set up host-only network on Ubuntu
{id: virtual-box-network-access-ubuntu}

```
  ifconfig -a
  sudo apt-get install ifupdown
  sudo apt-get install ssh
  edit /etc/network/interfaces  and add
       auto enp0s8
       iface enp0s8 inet static
       address 192.168.56.10
       netmask 255.255.255.0
```

```
Run sudo ifup enp0s8
```


## Install ssh server
{id: sshd}
{i: sshd}

```
$ sudo apt-get install ssh
$ ssh localhost
$ ifconfig | grep inet
```


## Set up ssh access
{id: exercise-ssh}

* Enable and set up ssh access to your virual environment.
* Set up the X server on your desktop.
* In /etc/ssh/sshd_config  make sure you have **X11Forwarding yes**
* **ssh -X IP**




## Exercise: Terminal
{id: exercise-terminal}

* Change your password.
* Launch Firefox.
* Print the path to the home directory.
* Flip through the documentation of man.



## Exercise: commands
{id: exercises-commands}

Try the following commands and try to understand that they do:


```
cal
cal 2000
cal 1 2000
cat /etc/passwd
curl http://google.com/
date
hostname
id
last
top       (q to quit)
uptime
who
whoami
history
```




