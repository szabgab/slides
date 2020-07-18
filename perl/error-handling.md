# Error Handling
{id: error-handling}





## Returning error status or throwing exception?
{id: perl5-returning-error-status}

```
foreach my $filename (@names) {
    my $fh = open_file($filename);
    my $data = read_file($fh);
}
```


What if open fails and the $fh is undef? Who will notice this problem?
Only in read_file we will notice it.



* Developer must work in order to ignore the exception
* Propagating exception upwards is easy: don't do anything



## eval block
{id: perl5-eval-block}
{i: eval}
![](examples/error/eval.pl)

* Simple
* built in the language
* but not powerful
* cannot pass context of the error, just a string



## Exception handling with Try::Tiny
{id: perl5-try-tiny}
{i: Try::Tiny}
{i: try}
{i: catch}
![](examples/error/try_tiny.pl)


## Carp
{id: perl5-carp}
{i: Carp}
{i: carp}
{i: croak}

```
It is better to use croak and carp instead of die and warn.
```
![](examples/error/carp.pl)
![](examples/error/Module.pm)


## Carp::Clan
{id: perl5-carp-clan}
{i: Carp::Clan}
![](examples/error/carp_clan.pl)
![](examples/error/App/Code.pm)
![](examples/error/App/Module.pm)



## The problem with die and croak
{id: perl5-the-problem-with-die-and-croak}

```
In both cases the error string defines the type of the error.
If we want to change the text, then in every place where we catch those
errors we have to update some regular expression.

Cannot easily propagate the context of the error as it is just a string.
```


## Exception::Class
{id: perl5-exception-class}
{i: Exception::Class}
{i: throw}
![](examples/error/exception.pl)
![](examples/error/Lottery.pm)
![](examples/error/Lottery/Exceptions.pm)


## Processing exceptions
{id: perl5-exception-class-processing-exceptions}

```
Make sure the exceptions are checked in growing order of generality.
First check for the most specific exceptions then for the more
generic ones.
```


## Exercise
{id: perl5-exercise-exceptions}

```
Take the examples/error/exception.pl file and add an exception class that 
checks if the given value was a number or not.

Add an exception class called Number::Bad and make Number::Small and
Number::Big subclasses of that class.
```


## Solution
{id: perl5-solution-exceptions-not-number}
![](examples/error/exception_not_number.pl)


## Solution
{id: perl5-solution-exceptions-bad-number}
![](examples/error/exception_bad_number.pl)



