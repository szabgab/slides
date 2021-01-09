# Advanced slides
{id: advanced-slides}


## Signals and the kill function
{id: signal-handlers}
{i: $SIG}
{i: %SIG}
{i: kill}

List of [signals on Linux](http://kernel.org/doc/man-pages/online/pages/man7/signal.7.html): `man -S 7 signal`

To send a signal use `kill SIG, LIST` (process IDs)

For example: `kill 9, $pid;`

![](examples/advanced-perl/signal.pl)

```
%SIG

$SIG{INT}  = sub { print "INT received\n";};         # kill -2  or Ctrl-C
$SIG{TERM} = sub { print "TERM received\n"; exit;};  # kill -15
$SIG{TSTP} = sub { print "TSTP received\n";};        # kill -20 or Ctrl-Z

$SIG{KILL} = sub { print "KILL received\n"; exit;};  # kill -9  cannot catch it


$SIG{$name} = 'IGNORE';             # to ignore it
$SIG{$name} = 'DEFAULT';            # to reset to the default behavior
```


## Catch Ctrl-C
{id: catch-ctrl-c}
![](examples/advanced-perl/catch_ctr_c.pl)


## Catch signals
{id: catch-signals}
![](examples/advanced-perl/catch_signals.pl)


## Exercise: Catch ctrl-c and ask continue or terminate?
{id: exercise-catch-ctrl-c}


Take the `examples/advanced-perl/catch_ctr_c.pl`
and change it so when the user presses Ctrl-C the counting
stops and the user is asked if she really wants
to terminate the program. (y/n).




If yes is given then quit. If no is given continue.




If Ctrl-c is pressed again later then ask again.




Make sure you do as little as possible in the actual signal handle.




## Solution: Catch ctrl-c and ask
{id: solution-catch-ctrl-c}
![](examples/advanced-perl/catch_ctr_c_confirm.pl)

See what happens if you don't set the SIG handler to IGNORE?


See what happens if you remove the word local?



## Always use strict and warnings
{id: use-strict-and-warninigs}
{i: strict}
{i: warnings}


Always start your Perl code with:



```
use strict;
use warnings;
```


Example code that generates warning:



Add code everywhere to avoid warnings:

![](examples/advanced-perl/code_with_warnings.pl)



## Avoid warnings
{id: avoid-warnings}
![](examples/advanced-perl/avoid_warnings.pl)


A lot of work. Cannot be done easily to an existing application.




## Turn off warnings selectively and in a small scope
{id: no-warnings}
{i: no warnings}
![](examples/advanced-perl/no_warnings.pl)

```
See
perldoc warnings       for the use of warnings
perldoc perllexwarn    for the warning categories
perldoc perldiag       for a list of warnings and errors
```


## Catch and log warnings
{id: catch-warnings}
{i: $SIG}
{i: __WARN__}
![](examples/advanced-perl/catch_warnings.pl)


%SIG holds all the signals perl can deal with with the two special signal handles __WARN__ and __DIE__
sub {} is an anonymous subroutine we will discuss later


![](examples/advanced-perl/catch_multiple_warnings.pl)


## splain and use diagnostics
{id: use-diagnostics}
{i: splain}
{i: diagnostics}

```
perl examples/advanced-perl/code_with_warnings.pl 2> err.txt
splain err.txt
```

The output looks like this:

```
Use of uninitialized value $total in addition (+) at
	examples/advanced-perl/use_diagnostics.pl line 15 (#1)
    (W uninitialized) An undefined value was used as if it were already
    defined.  It was interpreted as a "" or a 0, but maybe it was a mistake.
    To suppress this warning assign a defined value to your variables.

    To help you figure out what was undefined, perl will try to tell you the
    name of the variable (if any) that was undefined. In some cases it cannot
    do this, so it also tells you what operation you used the undefined value
    in.  Note, however, that perl optimizes your program and the operation
    displayed in the warning may not necessarily appear literally in your
    program.  For example, "that $foo" is usually optimized into "that "
    . $foo, and the warning will refer to the concatenation (.) operator,
    even though there is no . in your program.
```


Alternatively you could also insert the following in your code:
`use diagnostics;`
to get the explanations for every warning.
See also `perldoc perldiag` for a detailed explanation of each warning and error.


## Fatal warnings
{id: fatal-warnings}
{i: FATAL}

```
use warnings FATAL => 'all';
```


## Logging Exceptions
{id: logging-exceptions}
{i: __DIE__}

```
$SIG{__DIE__} = sub { logger('error', $_[0]) };
```
![](examples/advanced-perl/die_handler.pl)


## Always open files in the new way
{id: open-with-3-parameters}
{i: open}


Old way:


![](examples/advanced-perl/open_file_old.pl)

Recommended way:

![](examples/advanced-perl/open_file_new.pl)

```
Security problems.

Being global, difficult to pass as parameter to functions.
```

## Array slices
{id: array-slices}
{i: array slices}

![](examples/advanced-perl/array_slices.pl)

A few more examples

```
my @i = (3, 5, 7);
print "@i\n";                           # 3 5 7
print "@letters[@i]\n";                 # d f h
print "@letters[split ' ', '3 5 7']\n"; # d f h
```


## Array slices on the fly
{id: array-slices-on-the-fly}
![](examples/advanced-perl/array_slices_split.pl)


## Hash slices
{id: hash-slices}
{i: hash slices}
![](examples/advanced-perl/hash_slices.pl)


## Hash slices in assignment
{id: hash-slice-in-assignment}
![](examples/advanced-perl/hash_slices_assignment.pl)


## splice
{id: splice}
{i: splice}

![](examples/advanced-perl/splice.pl)

[Splice to slice and dice arrays in Perl](https://perlmaven.com/splice-to-slice-and-dice-arrays-in-perl)


## LIST and SCALAR context
{id: localtime-in-context}
{i: LIST}
{i: SCALAR}
{i: context}


See the behavior of `localtime()`.


![](examples/advanced-perl/localtime.pl)


How could we implement something similar?


## wantarray
{id: wantarray}
{i: wantarray}


When called within a function it will return undef, true or false
depending on how was the function called.


```
undef  if it was called in a void context like f();
true   if it was called in a list context like @x = f(); or print f();
false  if it was called in scalar context like $x = f(); or if($f()) {...}
```
![](examples/advanced-perl/wantarray.pl)


## wantarray example
{id: count-and-sum}

![](examples/advanced-perl/count_and_sum.pl)

See also `Want` and `Contextual::Return` for even more options.


## Slow sorting
{id: slow-sort}

The problem: bad performance

![](examples/advanced-perl/sort_files.pl)


## Speed up sorting
{id: speed-up-sorting}

Reduce the number of slow calls from `n**2` to `n`.

![](examples/advanced-perl/schwartzian_transformation_detailed.pl)


## Schwartzian transformation
{id: schwartzian-transformation}
![](examples/advanced-perl/schwartzian_transformation.pl)


## Compilation phases: BEGIN, CHECK, INIT, END
{id: perl-phases-begin-check-init-end}
{i: BEGIN}
{i: CHECK}
{i: INIT}
{i: END}

```
BEGIN {
    # do something here
}
```

```
* You can have more than one of each one

BEGIN  - execute as soon as possible (compiled)
CHECK  - execute after the whole script was compiled
INIT   - execute before running starts
END    - execute as late as possible (after exit() or die())

When running perl -c script.pl   both the BEGIN and CHECK blocks are executed.

perldoc perlmod
```
![](examples/advanced-perl/begin_end.pl)
![](examples/advanced-perl/begin_end.out)
![](examples/advanced-perl/phases.pl)
![](examples/advanced-perl/phases.out)


## AUTOLOAD
{id: autoload-in-perl5}
{i: AUTOLOAD}
{i: $AUTOLOAD}


![](examples/advanced-perl/no_autoload.pl)

```
Output:

Undefined subroutine &main::f called
```


{aside}
If you call a function that does not exist when the call is made, Perl will raise an `Undefined subroutine called` exception. If the exception is
not handled it will stop your program.

In the exception it will also give you the full name of the function that was missing. In the above case it will be `&main::f`.

With all the other magic, Perl also provides you a tool that will help you deal with such situations. You can include a block called AUTOLOAD
in your code and if AUTOLOAD {} is defined then it will be executed instead of every missing function. From that point your imagination is the
only limiting factor on how to handle the situation.
{/aside}

![](examples/advanced-perl/autoload.pl)

Output:

![](examples/advanced-perl/autoload.out)


## Static variable
{id: static-variable}
{i: static variable}

![](examples/advanced-perl/static.pl)



## Exercise: create counter
{id: exercise-create-counter}


Create a script with a function called count() which is capable of
maintaining several counters.


![](examples/advanced-perl/multi-counter-skeleton.pl)


## Solution: create counter
{id: solution-create-counter}
![](examples/advanced-perl/multi-counter.pl)


## Saved variable: local
{id: local-in-perl5}
{i: local}


Slurp mode used local $/ = undef;


![](examples/advanced-perl/local.pl)
![](examples/advanced-perl/local.out)
![](examples/advanced-perl/dumper_local.pl)
![](examples/advanced-perl/dumper_local.out)


## autodie
{id: autodie}
{i: autodie}

![](examples/advanced-perl/autodie.pl)


Can't open 'data.txt' for reading: 'No such file or directory' at examples/advanced-perl/autodie.pl line 7


## Modern::Perl
{id: modern-perl}
{i: Modern::Perl}

```
use Modern::Perl;
```

Loads strict, warnings, the features of 5.10 and the c3 Method Resolution Order

Check out the [Modern Perl book](http://www.onyxneon.com/books/modern_perl/index.html)


## Perl::Critic
{id: perl-critic}
{i: Perl::Critic}
{i: perlcritic}


Originally based on the Perl Best Practices by Damian Conway.
Written by Jeffrey Thalhammer.
Try [Perl::Critic](http://perlcritic.com/) online.


```
perlcritic -h
perlcritic -5 file_name.pl
```

## Perl::Tidy
{id: perl-tidy}
{i: Perl::Tidy}
{i: perltidy}

```
perltidy
```


## caller
{id: caller}
{i: caller}

![](examples/advanced-perl/caller.pl)


## Log::Dispatch
{id: log-dispatch}
{i: Log::Dispatch}
![](examples/advanced-perl/log_dispatch.pl)


## Log::Log4perl easy
{id: log4perl-easy}
{i: Log::Log4perl}
![](examples/advanced-perl/log4perl_easy.pl)
![](examples/advanced-perl/My/EasyApp.pm)

```
2014/08/24 08:02:52 This is fatal
2014/08/24 08:02:52 This is error
2014/08/24 08:02:52 This is warn
2014/08/24 08:02:52 FATAL from EasyApp
```


## Exercise: Log::Dispatch
{id: exercise-log-dispatch}


Take the examples/advanced-perl/log_dispatch.pl
and change it so only warnings are printed to the screen.
debug messages are printed to a log file.
The name of the file should be in the format YYYY-MM-DD.log
The log line should include the name file name and the line number where it was called.

Check out the strftime of the POSIX module and see how Log::Dispatch
allows you to provide a callback function.


## Solution Log::Dispatch
{id: solution-log-dispatch}
![](examples/advanced-perl/log_dispatch_extended.pl)



