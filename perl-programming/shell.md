# Shell to Perl
{id: shell-to-perl}

## Shell and Perl intro
{id: shell-and-perl-intro}

Manipulating Files and Directories


## File test or -X operators
{id: file-test}
{i: -e}
{i: -f}
{i: -d}
{i: -M}

```
Before we try to read from a file or try to write to a file
we might want to check our rights, if we can do the required action at all.

For this there is a bunch of so called -X operators. Usually you use them in
an if statement:
```

```
if (-e "file.txt") {
    print "File exists !\n";
}
```

* -e File (or directory) exists
* -r File (or directory) is readable by this user
* -w File (or directory) is writable by this user
* -x File (or directory) is executable by this user
* -f Entry is a file
* -d Entry is a directory
* -l Entry is a symbolic link
* -s Size of the file (hence also means 'file is not empty')
* -M Number of days between the modification date of a file and the start time of our script


```
Hence -s can be used either in an if statement or like this:
```

```
$size = -s $filename;
```

```
There are more such operators see <command>perldoc -f -x</command>
```



## Running External Programs
{id: running-external-programs}
{i: system}
{i: ``}
{i: qx}


<command>system()</command> can execute any external program. You pass to it the same
string as you would type on the command line.




It returns 0 on success and the exit code of the external program on failure.
Hence the strange way we check if it fails.




Passing the program name and the parameters as an array is more secure as it 
does not involve invocation of a shell. There is no shell processing involved;



```
system("some_app.exe --option");

```


See perldoc -f system for more error handling



```
my $result = `some_app.exe --option`;
my @result = `some_app.exe --option`;
```


backticks `` are also know as <emp>qx{}</emp>




## Open pipe for reading
{id: perl-open-pipe-for-reading}
{i: -|}

Connect to STDOUT of find

![](examples/shell/find_pipe.pl)


## Open pipe for writing
{id: perl-open-pipe-for-writing}
{i: |-}

Connect to STDIN of grep

![](examples/shell/pipe_grep.pl)


## Pager
{id: command-line-pager}

Connect to STDIN for paging

![](examples/shell/page.pl)


## sendmail.pl
{id: sendmail-with-perl}

Connect to STDIN of sendmail

![](examples/shell/sendmail.pl)


## UNIX commands from the inside
{id: unix-commands-in-perl}
{i: unlink}
{i: rm}
{i: del}
{i: rename}
{i: chmod}
{i: chown}
{i: cd}
{i: chdir}
{i: rmdir}
{i: ln}
{i: link}
{i: symlink}
{i: readlink}
{i: glob}
{i: %ENV}
{i: $ENV{HOME}}

```
You can run every external command using <emp>system</emp> 
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


## File globbing (wildcards)
{id: file-globbing}

![](examples/shell/file_globbing.pl)


## Rename files
{id: rename-files}
{i: ls}

* glob - directory listing

![](examples/shell/rename_files.pl)


## Directory handles
{id: directory-handles}
{i: opendir}
{i: readdir}

For a platform independent approach use opendir and readdir.

In order to read the content of a directory (that is the list of the files)
first we have to open the directory similarly to the way we opened a file
but using the opendir function
This way we get a directory handle which we can use in subsequent operations.

Once the directory was opened successfully we can use the function readdir
in a loop to get the names of the files in that directory

![](examples/shell/list_directory.pl)

in LIST context readdir returns all the files in the directory.

```
opendir(my $dh, "/etc") or die $!;
@files = readdir $dh;
```


## File::HomeDir
{id: file-homedir}

![](examples/shell/file_homedir.pl)


## More UNIX commands implemented in modules
{id: more-unix-commands-in-perl}
{i: pwd}
{i: cwd}
{i: basename}
{i: dirname}
{i: cp}
{i: copy}
{i: mv}
{i: move}
| Module | Usage | Comment |
| Cwd | $dir = cwd; | current working directory |
| File::Copy | copy "oldfile", "newfile"; |  |
|  | move "oldfile", "newfile"; | this works between file systems as well |
| File::Basename | basename "/a/b/c/file.pl"; | file.pl |
|  | dirname "/a/b/c/file.pl"; | /a/b/c |
| File::Path | mkpath("a/b/c") | (like mkdir -p) |
|  | rmtree("/") |  |
| File::Find |  |  |
| File::Find::Rule |  |  |


## File::Spec
{id: more-file-modules}
{i: File::Spec}
{i: catfile}
![](examples/shell/file_spec.pl)


```
use File::Spec::Functions;

my $f = catfile($dir, 'admin', 'project.txt');
```


## Change Copyright text in every source file in a directory hierarchy
{id: file-find}
{i: File::Find}
{i: find}

* File::Find
* reference to subroutine

![](examples/shell/change_files.pl)


## Exercise: Tree
{id: exercise-tree}
{i: tree}

```
Implement tree: prints a tree structure of a given directory.
All filenames are printed and subdirectories are properly indented.
$ tree.pl .
```

```
.
  subdir_1
    file_1_in_subdir_1
    file_2_in_subdir_1
  subdir_2
    subdir_2_1
      file_1_in_subdir_2_1
    file_1_in_subdir_2
```

```
Implement the previous one using File::Find
```

```
Implement the previous one using File::Find::Rule
```


## Exercise: Check for UID 0
{id: exercise-check-for-uid-0}


In UNIX/Linux the information about users is kept in the
/etc/passwd file. Each line represents a user. The fields
in each line are as follows:
<command>username, password,UID,GID,Gecos,home directory,shell</command>
Today the passwords are usually kept separately hence in this file you will only
see an x in the second field.




When someone breaks in to a UNIX/Linux machine she might try to
setup a user with UID 0 in order to gain root (superuser) access
to the machine. Please check the following file 
and print a message if there is a user with 0 as UID which is NOT
the root user.


![](examples/shell/etc_passwd.txt)


## Exercise: CPU load
{id: exercise-cpu-load}


Check if the load on the computer is over a certain threshold and log the
event to syslog. See the  3rd number from the right of the uptime command 
or the first number in the /proc/loadavg file on linux. 
The file looks like this:



```
0.15 0.26 0.72 1/128 9230
```


A sample file




## Exercise: MANIFEST file
{id: exercise-manifest}


We have a file called MANIFEST listing all the required 
files in a distribution. One file on every line.




Check if all the file exist.




Check if there are files that are not listed in MANIFEST




Optionally allow for wildcards in the file ?




Example MANIFEST file:


![](examples/shell/package/MANIFEST)


Expected solution:



```
File 'Makefile.PL' listed in MANIFEST is missing from package
File 'CHANGES' on disk but is not listed in MANIFEST
```



## Solutions: Tree
{id: solution-tree}
{i: File::Find}
{i: File::Find::Rule}
![](examples/shell/tree.pl)
![](examples/shell/tree_ff.pl)
![](examples/shell/tree_file_find_rule.pl)


## Solutions: Check for UID 0
{id: solution-check-for-uid-0}
![](examples/shell/uid_zero.pl)


## Solution: CPU load
{id: solution-cpu-load}
![](examples/shell/check_cpu_load.pl)


## Solution: MANIFEST file
{id: solution-manifest}
![](examples/shell/check_manifest.pl)




