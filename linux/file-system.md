# Navigating the File System
{id: linux-file-system}

## File system types
{id: filesystem-types}

* MS-DOS (FAT32)
* HPFS
* NTFS
* ...



* ext3
* **ext4**
* ResierFS
* ...




## Linux file system structure
{id: linux-filesystem-structure}

```
/
  bin/
  boot/
  dev/
  etc/
  home/
    foo/
    bar/
  lib/
  lost+found/
  media/
  mnt/
  opt/
  proc/
  root/
  sbin/
  tmp/
  usr/
  var/
```

Some parts might be mounted from other disk or even from other computers. This is transparent for us.



## Show directory tree
{id: show-directory-tree}
{i: tree}

```
tree
tree -L 1 /
tree -L 2 -d /
```


## Current Working directory
{id: current-working-directory}
{i: pwd}

```
pwd        print working directory
```


## Directory listing - ls
{id: ls}
{i: ls}

```
ls        "default" listing
ls /bin

ls -1     one-column listing
ls -l     long listing with file-types and rights
ls -a     all, including hidden files
ls -A     all, except . and ..

ls -l
ls -ld    the directory
ls -ltr   long, sort by time, reverse
ls -i     show inodes
```


## File types
{id: file-types}

* - - Regular files
* d - Directories
* l - Symbolic links
* c - Character special files (e.g. tty: /dev/tty )
* b - Block special files (eg. disks: /dev/sda )
* s - Sockets
* p - Named pipe




## Hidden files
{id: hidden-files}
{i: .}

Files that the name start with a dot. By accident.




## Change Directory
{id: change-directory}
{i: cd}

```
cd         cd to home
cd ~       cd to home
cd ~joe    cd to the home of joe
cd ..      cd to parent directory
cd -       cd back to previous directory
```



## Display disk usage statistics
{id: display-disk-usage-statistics}
{i: du}

```
$ du
344   ./build/html/tucs/css
48    ./build/html/tucs/js
1520  ./build/html
400   ./build/linux/examples
696   ./build/linux
2288  ./build
272   ./examples/script
424   ./examples
2840  .
```


```
$ du -h      (human-readable)
172K    ./build/html/tucs/css
 24K    ./build/html/tucs/js
760K    ./build/html
200K    ./build/linux/examples
348K    ./build/linux
1.1M    ./build
136K    ./examples/script
212K    ./examples
1.4M    .
```


## du -s
{id: du-s}

```
$ du -hs *          (human-readable, summarize)
4.0K    README
1.1M    build
212K    examples
 24K    intro.xml
4.0K    linux.yml
 16K    scripts.xml
4.0K    variables.xml
```


```
$ du -s * | sort -n -r
2288    build
424     examples
48      intro.xml
32      scripts.xml
8       variables.xml
8       linux.yml
8       README
```


## Display free disk space using df
{id: display-free-disk-space}
{i: df}

```
$ df
Filesystem     1K-blocks      Used Available Use% Mounted on
/dev/sda1       47931368  18992880  26480628  42% /
none                   4         0         4   0% /sys/fs/cgroup
udev             2009680         4   2009676   1% /dev
tmpfs             404732      1276    403456   1% /run
none                5120         0      5120   0% /run/lock
none             2023660       144   2023516   1% /run/shm
none              102400        28    102372   1% /run/user
/dev/sda5      413296896 371702128  20577416  95% /home
```


## Disk layout
{id: disk-layout}

```
$ df
Filesystem     1K-blocks      Used     Available    Use%   Mounted on
/dev/sda1     40,720,960   5,282,552   35,422,024   13%    /
```

38 Gb


* Partitions
* Block size (1K)
* Inode table and Inodes


```
$ df -i
Filesystem      Inodes      IUsed       IFree   IUse%   Mounted on
/dev/sda1      4,807,680   196,498   4,611,182    5%    /
```



## Free Disk space with human readable numbers
{id: df-h}

```
$ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        46G   19G   26G  42% /
none            4.0K     0  4.0K   0% /sys/fs/cgroup
udev            2.0G  4.0K  2.0G   1% /dev
tmpfs           396M  1.3M  394M   1% /run
none            5.0M     0  5.0M   0% /run/lock
none            2.0G  144K  2.0G   1% /run/shm
none            100M   28K  100M   1% /run/user
/dev/sda5       395G  355G   20G  95% /home
```


## Show inodes stats: df -hi
{id: df-hi}

```
$ df -hi
Filesystem     Inodes IUsed IFree IUse% Mounted on
/dev/sda1        3.0M  587K  2.4M   20% /
none             495K     2  495K    1% /sys/fs/cgroup
udev             491K   533  491K    1% /dev
tmpfs            495K   555  494K    1% /run
none             495K     3  495K    1% /run/lock
none             495K     4  495K    1% /run/shm
none             495K    14  495K    1% /run/user
/dev/sda5         26M  737K   25M    3% /home
```


## mounting external disks
{id: mounting}
{i: mount}
{i: umount}

* NFS - Network File System
* Samba (SMB) - Microsoft Network
* mount, umount, /etc/fstab



## Exercise: File system
{id: exercise-filesystem}

* Create a file called      this is a long file with some spaces.txt
* Rename it to              not so long.txt



## Exercise: Explore /proc
{id: exercise-proc}

The /proc directory has a lot file-looking entitities that hold a lot of information
about the system. Explore them and share your findings with us. For examply try to run
<command>cat /proc/meminfo</command>.








