# stat, lstat

* stat
* lstat


In order to get information from the inode table you can use the stat system call

```
 ARRAY = stat FILEHANDLE| FILENAME
```

```
 @fields = stat ($filename);
 @fields = stat ($fh);

 $fields[4]  is the UID
 $fields[7]  is the size in bytes
```

```
  0 dev      device number of file system
  1 ino      inode number
  2 mode     file mode  (type and permissions)
  3 nlink    number of (hard) links to the file
  4 uid      numeric user ID of file's owner
  5 gid      numeric group ID of file's owner
  6 rdev     the device identifier (special files only)
  7 size     total size of file, in bytes
  8 atime    last access time in seconds since the epoch
  9 mtime    last modify time in seconds since the epoch
 10 ctime    inode change time (NOT creation time!) in seconds since the epoch
 11 blksize  preferred block size for file system I/O
 12 blocks   actual number of blocks allocated

 for symbolic links use lstat
```


