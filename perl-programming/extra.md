# Extra slides
{id: extra-slides}





## List all defined variables
{id: list-all-defined-variables}

![](examples/subroutines/list_defined_variables.pl)


## Perl internal variables
{id: perl-internal-variables}


* $! - error of the last system call e.g. [open file](https://perlmaven.com/beginner-perl-maven-no-such-file).
* $/ - input record separator, [slurp mode](https://perlmaven.com/slurp).
* $_ - the [default variable](https://perlmaven.com/the-default-variable-of-perl) for many operations.
* $0 - Name of the current program.
* $1, $2, .. Regex match variables.
* $] - version number of Perl
* $a, $b - variables of sort.
* @ARGV - command line parameters.
* @_ - parameters of the current function.
* @INC - list of directories to search for modules.
* %INC - loaded modules and the path to them on the disk.
* %ENV - environment variables
* %SIG - signal handlers
* Full list at [perldoc perlvar](https://metacpan.org/pod/distribution/perl/pod/perlvar.pod)




## What is Perl ?
{id: what-is-perl}

* Created by Larry Wall in 1987
* Scripting language replacing awk, sed and shell scripts
* Glue language - putting together tools provided for the OS
* Free software distributed under GPL and the Artistic licenses

* Available for most of the platforms (UNIX/Linux/Windows/Macintosh/VMS/main frame/...)
* Generally speaking machine and OS independent but the system calls are OS specific

* Interpreted language compiled to a machine independent byte tree and ... 
* ... Executed immediately by the interpreter
* C-like syntax



## What does Perl stand for ?
{id: perl-backronym}

* Perl is not an acronym it is what we call a backronym
* Practical Extraction and Reporting Language
* Pathologically Eclectic Rubbish Lister
* Objective: Making Easy Things Easy and Difficult Things Possible
* Motto: TMTOWTDI = There's More Than One Way To Do It



## Scripting language ?
{id: scripting-language}


Some people talk about writing code in Perl as scripting and others as programming.
Some say Perl is a scripting language others that it is a programming language.




Actually there is no such definition as scripting language. The real definitions are:



* Compiled languages
* Interpreted languages



## Is Perl Interpreted or Compiled Language
{id: compiled-interpreted}

* Compiled languages: C, C++
* Compiled and interpreted languages: Java, Perl
* Interpreted languages: BASIC (or Shell)



Perl is in the middle as it is compiled to a byte tree (similarly to Java)
that is never saved as a file. It also requires the interpreter to be available
with the Perl program.




Advantages of a compiled language:



* Can be faster especially in short applications
* Does not need a compiler/interpreter/Virtual Machine on the users machine (it can be distributed on its own)



Disadvantages of a compiled language:



* It has to be compiled separately to every platform
* Difficult to make it platform independent



## Why use Perl ?
{id: why-use-perl}

* Easy  - for daily use
* Nearly unlimited - for high-level programming (no real time, no kernel, no device drivers please)
* Mostly fast - fast enough for the tasks you would do with Perl
* Can solve problems - the symbol of Perl is the camel, ugly but can handle difficult environment



## What is it good for ?
{id: what-is-perl-good-for}

* QA (test automation)
* System Administration
* Configuration Management
* Web backend (CGI/Database access)
* Quick and dirty programs (automating simple daily jobs)
* Biotechnology
* Prototypes



## Its strengths
{id: strengths-of-perl}

* Text processing (pattern matching)
* List processing
* Database access
* System language



## Redirection by the user
{id: redirection}

```
In order to read a real file we have to wait for a later chapter or you can ask 
the user of the script to use redirection on the command line.

The user of out program might do the following to redirect the input
and/or the output of our program.

myperl.pl &lt; in.txt
myperl.pl &gt; out.txt
myperl.pl &lt; in.txt  &gt; out.txt
```


## for loop
{id: for-loop}
{i: for}

```
for (INITIALIZE; TEST; INCREMENT) {
    BODY;
}

for (my $i=0; $i &lt; 10; $i++) {
     print "$i\n";
}

# but a foreach loop might be better for the same looping:
foreach my $i (0..9) {
    print "$i\n";
}
```


## ASCII table
{id: ascii-table}
{i: chr}
{i: ord}

```
foreach my $i (32..128) {
	print $i, " ", chr($i), "\n";
}

                           # the inverse function is ord()
print ord('a');            # 97
```


## default variable $_
{id: topic}
{i: $_}


Default variable



```
my @fruits = qw(apple banana peach);
foreach my $fruit (@fruits) {
	print $fruit;
}
```

```
foreach my $name (@people) {
    print $name;
}

foreach (@people) {
    print;
}

foreach $_ (@people) {
    print $_;
}
```


## Return values
{id: return-values}

Perl functions always returns a value.
Either explicitly by  calling return or
the result of the last computation.

![](examples/subroutines/return_value.pl)

Solving the above problem: always use `return`
Add `return $i;` before the end of the subroutine.


## UNIX file system, hard links symbolic links
{id: unix-file-system}

* What is in a Directory ?
* What is in an Inode ?
* What is a symbolic link ?
* What is a hard link ?


```
What links can be between different partitions ?

(hint: only symbolic links as hard links are bound to the inode
number which is local to each partition)
```


## stat, lstat
{id: stat-lstat}
{i: stat}
{i: lstat}


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


## Compare values
{id: compare-values}
![](examples/scalars/compare_values.pl)


## Bitwise Operations
{id: perl-bitwise-operations}
{i: bitwise}
{i: &amp;}
{i: |}
{i: ~}
{i: ^}
{i: &lt;&lt;}
{i: &gt;&gt;}

```
The following operators work on the binary representation of the values

 &amp;    AND
 
 |    OR

 ^    XOR

 ~    NOT  (complement)

 >>   right shift

 &lt;&lt;   left shift
```


## bitwise examples
{id: perl-bitwise-examples}
![](examples/other/bitwise.pl)


## Filename creation based on date
{id: filename-with-timestamp}

```
 # creating a filename based on the date YYYY-MM-DD-HH-MM-SS 
 @t = (localtime)[5,4,3,2,1,0];
 $t[0]+=1900;
 $t[1]++;
 $filename = sprintf "%d-%0.2d-%0.2d-%0.2d-%0.2d-%0.2d", @t;
```



## Debugging prints
{id: debugging-prints}

```
# Scalar:
print STDERR "Debug: '$a'\n";


# Array:
print STDERR "Debug: @a\n";

print STDERR "Debug: ", join "|", @a, "\n";


# Hash:
print STDERR "Debug: ", join "|", %h, "\n";

print STDERR "Debug: "; 
foreach (keys %h) { print STDERR "$_=>$h{$_}|";
print STDERR "\n";


print STDERR "Debug: "; 
print STDERR "$_=>$h{$_}|" for keys %h;
print STDERR "\n";
```


## Where is perl installed on your system ?
{id: where-is-perl-installed}

It can be installed in any place but usually you'll find it in one of the
following places:

on UNIX:

```
/usr/bin/perl
/usr/local/bin/perl
```

on Windows:

```
c:\perl\bin\perl.exe
```

In addition you'll find a bunch of Perl standard modules installed somewhere
on the system.


## Send e-mail
{id: send-email}
{i: mail}
{i: sendmail}
{i: Mail::Sendmail}

* Mail::Sendmail

![](examples/applications/sendmail.pl)




