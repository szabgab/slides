# UNIX commands from the inside

* unlink
* rm
* del
* rename
* chmod
* chown
* cd
* chdir
* rmdir
* ln
* link
* symlink
* readlink
* glob
* %ENV
* $ENV{HOME}

```
You can run every external command using `system`
but it makes it platform dependent and might have more security implications.

The following calls are available from Perl.
There are more but we won't cover them now.
```
|  |  | UNIX | DOS |
| unlink | FILENAME | rm | del |
| rename | OLDFILE, NEWFILE | mv | ren |
| chmod | MODE, FILE | chmod | - |
| chown | UID, GID, FILE | chown | - |
| chdir | DIRNAME | cd | cd |
| mkdir | DIRNAME, PERM | mkdir | mkdir |
| rmdir | DIRNAME | rmdir | rmdir |
| link | OLDNAME, NEWNAME | ln | - |
| symlink | OLDNAME, NEWNAME | ln -s | - |
| readlink | LINKNAME | ls -l | - |
| glob | WILDCARDS | ls -1 | dir |
| opendir, readdir |  | ls -1 | dir |
| %ENV, $ENV{HOME} |  |  |  |

```
my $uid = getpwnam($username);
my $gid = getgrnam($groupname);
```

[How to remove, copy or rename a file with Perl](https://perlmaven.com/how-to-remove-copy-or-rename-a-file-with-perl)


