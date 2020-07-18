# Advanced Arrays
{id: advanced-arrays}


## The year 19100
{id: localtime}


First, let's talk about time.


{i: time}
{i: localtime}
{i: gmtime}

```
$t = time();         # 1021924103
                     # returns a 10 digit long number,
                     # the number of seconds since 00:00:00 UTC, January 1, 1970

$x = localtime($t);  # returns a string like           Thu Feb 30 14:15:53 1998
$z = localtime();    # returns the string for the current time

$z = localtime(time - 60*60*24*365);
   # returns the string for a year ago, same time, well almost

@y = localtime($t);  # an array of time values:
                     # 53 15 14 30 1 98 4 61 0
                     # the 9 values are the following:

#  0    1    2     3     4    5     6     7     8    (the index)
($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);

# The localtime function is aware of what is on the left side of the = sign !!!!
```


```
# OK but where does that 19100 come from ?
$mon  0..11
$min  0..59
$sec  0..60
$year YEAR-1900         # for example 2000-1900 = 100
                        # but people used  "19$year"   instead of 1900 + $year
                        # which is          19100      instead of 2000
```


gmtime is the same just gives the time as it is in Greenwich.
[The year of 19100](https://perlmaven.com/the-year-19100)




## SCALAR and LIST Context
{id: scalar-and-list-context}
{i: SCALAR context}
{i: LIST context}

```
my @a = ("zero", "one", "two", "three");
my @b = @a;           # LIST context
my $c = @a;           # SCALAR context

if (@a) {
}

while (@a) {
}
```

[Scalar and List context in Perl](https://perlmaven.com/scalar-and-list-context-in-perl)





## Context Sensitivity
{id: context-sensitivity}
{i: scalar()}

```
Every operator creates a 'context' let's see a few examples

Assignment to a scalar variable creates SCALAR context:
$x = localtime();
$x = @z;
$x = SCALAR

Assignment to an array creates LIST context:
@y = localtime();
@y = @z;
@y = LIST
```


```
                            # Expressions providing SCALAR context
$x = SCALAR;
$y[3] = SCALAR;
8 + SCALAR
"Foo: " . SCALAR
if (SCALAR) { ... }
while (SCALAR) { ... }
scalar(SCALAR)

                            # Expressions providing LIST context:
@a = LIST;
($x, $y) = LIST;
($x) = LIST;
foreach $x (LIST) {...}
join ";", LIST
print LIST

                            # example
@a = qw(One Two Three);
print @a;                   # OneTwoThree       print LIST
print 0 + @a;               # 3                 SCALAR + SCALAR
print scalar(@a);           # 3                 scalar(SCALAR)
```

see also `perldoc -f function-name`


## Filehandle in scalar and list context
{id: filehandle-in-scalar-and-list-context}

![](examples/perlarrays/filehandle_in_context.pl)


## slurp mode
{id: slurp-mode}
{i: $/}
{i: slurp}
![](examples/perlarrays/slurp.pl)


## File::Slurp
{id: file-slurp}
{i: File::Slurp}
{i: slurp}
![](examples/perlarrays/file_slurp.pl)


## Diamond operator
{id: diamond-operator}
![](examples/perlarrays/diamond.pl)


## pop, push
{id: pop-push}
{i: pop}
{i: push}
![](examples/perlarrays/pop_push.pl)
![](examples/perlarrays/data.txt)


## push example
{id: push-example}
![](examples/perlarrays/collecting_data.pl)


## stack (pop, push) Reverse Polish Calculator
{id: stack-implementation}
{i: stack}
![](examples/perlarrays/reverse_polish_calculator.pl)


## shift, unshift
{id: shift-unshift}
{i: shift}
{i: unshift}
![](examples/perlarrays/shift_unshift.pl)

```
FIRST = shift ARRAY;
unshift ARRAY, VALUEs;
```


## queue (shift, push)
{id: queue-implementation}
{i: queue}
![](examples/perlarrays/queue.pl)



## shift
{id: shift-argv}
![](examples/perlarrays/shift_argv.pl)

```
shift defaults to shift @ARGV

Another usage of the short circuit

Slight bug.
Does it matter?
```


## reverse
{id: reverse}
{i: reverse}
![](examples/perlarrays/reverse.pl)


## Sort
{id: sort}
{i: sort}
{i: $a}
{i: $b}
{i: cmp}
{i: &lt;=&gt;}
{i: spaceship operator}

![](examples/perlarrays/sort.pl)

[Sorting arrays in Perl](https://perlmaven.com/sorting-arrays-in-perl)


## Ternary operator
{id: ternary-operator}
{i: ternary operator}
{i: ? :}

```
my $var;
if (COND) {
    $var = A;
} else {
    $var = B;
}

my $var = COND ? A : B;
```


## Count digits
{id: count-digits}
![](examples/perlarrays/count_digits.txt)
![](examples/perlarrays/count_digits.pl)



## Exercise: Color selector
{id: exercise-color-selector-files}


Take the solution from the previous chapter (you can use the file examples/perlarrays/color_selector.pl )
and add the following features:



1. Read the names of the colors from a file called colors.txt
1. Let the user pass the name of the color file using the **--filename FILENAME** option.



## Exercise: sort numbers
{id: exercise-sort-numbers}

Take the file `examples/perlarrays/count_digits.txt`
from the previous example and sort the numbers (not the digits).


## Exercise: sort mixed string
{id: exercise-sort-mixed-string}

In a file we have the string where each string has
a single letter at the beginning and then a number.
Sort them based on the number only, disregarding the letter.

Input:


```
A4
B1
A27
A3
```

Expected output:


```
B1
A3
A4
A27
```

File:


![](examples/perlarrays/sort_mixed_strings.txt)

Expected output from sample file

![](examples/perlarrays/sort_mixed_strings.out)


## Exercise: sort mixed string 2
{id: exercise-sort-mixed-string-2}


Take the above example and change it so now we'll take in account the letter too.
Sort the strings based on the first letter, and among values with the same
leading letter, sort them according to the numbers.



Input


```
A4
B1
A3
A27
```

Expected output


```
A3
A4
A27
B1
```

Expected output from sample file

![](examples/perlarrays/sort_mixed_strings2.out)


## Solution: color selector files
{id: solution-color-selector-files}
![](examples/perlarrays/color_selector_files.pl)


## Solution: sort numbers
{id: solution-sort-numbers}
![](examples/perlarrays/sort_numbers.pl)



## Solution: sort mixed strings
{id: solution-sort-mixed-strings}
![](examples/perlarrays/sort_mixed_strings.pl)


## Solution: sort mixed strings
{id: solution-sort-mixed-strings-2}
![](examples/perlarrays/sort_mixed_strings2.pl)


## List::Util
{id: list-util}


[List::Util](https://metacpan.org/pod/List::Util) provides functions such as

* max
* min
* sum

It resides in a distribution called [Scalar-List-Utils](https://metacpan.org/release/Scalar-List-Utils)


## Advanced: Multi dimensional array
{id: multi-dimensional-array}
{i: \@}

![](examples/perlarrays/matrix.pl)
![](examples/perlarrays/matrix.out)

```
Actually what we have is a simple array and each element of that
array can be another (anonymous) array (reference).
```




