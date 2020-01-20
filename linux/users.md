# Users
{id: users}

## Overview
{id: users-overview}

* users
* groups
* permissions



## /etc/passwd
{id: etc-passwd}
{i: /etc/passwd}
![](examples/etc/passwd)


## User properties
{id: user-properties}

* Username
* Password
* UID - user id
* GID - primary group id
* GECOS (free text details)
* Home directory  (/home/username).
* Default shell (/bin/bash).



## /etc/group
{id: etc-group}
{i: /etc/group}
![](examples/etc/group)

* Group name
* ?
* GID - Group ID
* Additional Members



## /etc/shadow
{id: etc-shadow}
{i: /etc/shadow}
![](examples/etc/shadow)


## User manipulation
{id: user-manipulation-front-end}

* useradd - low level utility to add user
* adduser - Perl script wrapping useradd
* usermod - 
* userdel



## Group manipulation
{id: group-manipulation-front-end}

* groupadd - low level utility to add group
* addgroup - Perl script wrapping groupadd
* groupmod
* groupdel



## /etc/skel
{id: etc-skel}

Files to be copied to the home directory when a new user is added.


```
ls -l1 /etc/skel/
.bash_logout
.bashrc
.profile
.Xresources
```


## /etc/profile
{id: etc-profile}
{i: /etc/profile}
{i: /etc/profile.d/}
{i: ~/.profile}

* /etc/profile - System-wide profile loaded when user logs in and loads the files in:
* /etc/profile.d/* 
* ~/.profile  - User specific profile



## Changing password
{id: passwd}
{i: passwd}

* Change user's own password.
* Change the password of other users (privileged).
* Lock out user.



## Change shell - chsh
{id: chsh}
{i: chsh}
{i: /etc/passwd}
{i: /etc/shells}

Updates /etc/passwd with one of the entries from /etc/shells


```
$ chsh -s SHELL
```





