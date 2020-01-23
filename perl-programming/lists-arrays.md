# Lists and Arrays
{id: lists-arrays}

## Lists and Arrays intro
{id: lists-arrays-intro}

While a scalar is single value a list is a bunch of single values.
A scalar value can be stored in a scalar variable.
A list can be stored in a list variable. It is called and array.


## List Literals, list ranges
{id: lists}
{i: ()}
{i: ..}
{i: qw}

```
A list is an ordered series of scalar values separated by comma and enclosed in parentheses.
The scalar values themselves can be references to other data structures.
(An array, explained later is a variable holding the content of a list.)
Examples of lists:
```


```
(1, 5.2, "apple pie")      # 3 values
('string', 42, 2.3, undef, ['one', 'two'], { 'name' => 'Foo Bar' })  # 6 values

($x, $y, $z)          # We can also use scalar variables as elements of a list
($x, 3, "foobar")     # or we can mix them
```



Special case, all of them "words":




```
("apple", "banana", "peach", "blueberry")   # is the same as
qw(apple banana peach blueberry)            # quote word
```



Special case, range operator:




```
(1 .. 10)                # same as
(1,2,3,4,5,6,7,8,9,10)
```

[Perl Arrays](https://perlmaven.com/perl-arrays)


## List Assignment
{id: list-assignments}

```
my ($x, $y, $z);

my ($x, $y, $z) = (1, "apple pie", 3.14);

($x, $y, $z) = f();   # where f() returns (2, 3, 7);
                      # nearly the same as $x=2; $y=3; $z=7;
($x, $y, $z) = f();   # where f() returns (8, 1, 5, 9);
                      # ignore 9
($x, $y, $z) = f();   # where f() returns (3, 4);
                      # $z will be undef
```

```
A regular question on job interviews:
How can we swap the values of 2 variables, let say $x and $y?
```


## loop over elements of list with foreach
{id: foreach-list}
{i: foreach}
{i: for}

* list
* foreach ITEM (LIST) {BLOCK}
* my - in the foreach loop

![](examples/arrays/list_colors.pl)

```
Blue
Yellow
Brown
White
```


## Create an Array, loop over with foreach
{id: foreach-array}
{i: @}
![](examples/arrays/list_colors_array.pl)

```
Blue Yellow Brown White
Blue
Yellow
Brown
White
```

[Perl for loop explained with examples](https://perlmaven.com/for-loop-in-perl)


## Array Assignment
{id: array-assignment}


You can also mix the variables on the right side
and if there are arrays on the right side the whole thing becomes one flat array !


![](examples/arrays/assignment.pl)


```
my ($x, @y, @z);
($x, @y)     = f(); # where f() returns (1, 2, 3, 4);
                    # $x is 1;  @y is (2, 3, 4)
($x, @y, @z) = f(); # where f() returns (1, 2, 3, 4);
                    # $x is 1;  @y is (2, 3, 4)  @z is empty: ()

@z = ();            # Emptying an array
```


## Debugging an array
{id: debug-array}
{i: Data::Dumper}
{i: Dumper}
{i: \@}

![](examples/arrays/debug.pl)

```
Moose Barney Foo Bar
Moose Barney Foo Bar
$VAR1 = [
          'Moose',
          'Barney',
          'Foo',
          'Bar'
        ];
$VAR1 = [
          'Moose',
          'Barney',
          'Foo Bar'
        ];
```


## foreach loop on numbers
{id: foreach-number}

```
foreach my $i (1..10) {
    print "$i\n";
}
```

```
1
2
3
4
5
6
7
8
9
10
```


## Array index (menu)
{id: array-index}
{i: $#array}
{i: $array[0]}

* $#array - the largest index
* $array[1] - array elements are scalar

![](examples/arrays/color_menu.pl)
{i: $array[-1]}


## Load Module
{id: array-index-checked}
{i: Scalar::Util}
{i: looks_like_number}
{i: is_number}

* looks_like_number

![](examples/arrays/color_menu_checked.pl)


## Command line parameters
{id: command-line-parameters-argv}
{i: @ARGV}
{i: $0}

* @ARGV - all the arguments on the command line
* $ARGV[0] - the first argument
* $0 - name of the program
* **perl read_argv.pl blue**

![](examples/arrays/read_argv.pl)


## Process command line parameters, use modules
{id: process-command-line-parameters}
{i: use}
{i: \|reference}
{i: Getopt::Long}

* scalar reference
* **perl process_command_line.pl --color blue**

![](examples/arrays/process_command_line.pl)


## Module documentation
{id: module-documentations}


[perldoc Getopt::Long](https://metacpan.org/pod/Getopt::Long)

[perldoc Cwd](https://metacpan.org/pod/Cwd)


## process CSV file
{id: split-strings}
{i: split}
{i: CSV}

* split

![](examples/arrays/process_csv_file.csv)
![](examples/arrays/process_csv_file.pl)



## process csv file (short version)
{id: process-csv-files-short}
![](examples/arrays/process_csv_file_short.pl)

```

Use the following command to run the script:

<command>perl examples/arrays/process_csv_file_short.pl examples/arrays/process_csv_file.csv</command>

```


## One-liner sum numbers in CSV file
{id: oneliner-sum-numbers-in-csv}

```
<command>perl -n -a -F; -e '$sum += $F[2]; END {print $sum}' examples/arrays/process_csv_file.csv</command>

-n  = loop over lines but do NOT print them 
-a  = autosplit by ' ' and assign to @F
-F; = replace the split string by ';'

The END block gets executed at the end of the execution and only once.
```




## process csv file using Text::CSV
{id: process-csv-file}
{i: Text::CSV}
{i: Text::CSV_XS}

```
What if there is a field with embedded comma (,)?
```
![](examples/arrays/process_csv_file_module.csv)
![](examples/arrays/process_csv_file_module.pl)


## process csv file using Text::CSV
{id: process-csv-file-newline}
{i: Text::CSV}
{i: Text::CSV_XS}

```
What if there is a field with embedded newline?
```
![](examples/arrays/process_csv_file_module_newline.csv)
![](examples/arrays/process_csv_file_module_newline.pl)


## Join
{id: join-lists}
{i: join}

```
my @fields = qw(Foo Bar foo@bar.com);
my $line = join ";", @fields;
print "$line\n";     # Foo;Bar;foo@bar.com
```

[join](https://perlmaven.com/join)


## Labels
{id: labels}


Normally the last and next keywords are related to the innermost loop.
In some cases that's not good. Perl allows us to define labels in front
of loops and then to use those labels in conjunction with last or next to
go to the last or next iteration of the specified loop.


![](examples/arrays/labels.pl)


## Exercise: Make the color selector user friendly
{id: exercise-user-friendly-color-selector}


Take the examples/arrays/process_command_line.pl script
( the color selector ) and make it more user friendly
by showing the numbers starting from 1 (and not from 0).




## Exercise: improve the color selector
{id: exercise-color-selector}


Take the examples/arrays/process_command_line.pl
script and improve it in several ways:



1. Check if the value given on the command line is indeed one of the possible values and don't let other colors pass.
1. Allow a --force flag that will disregard the previously implemented restriction. Meaning 
1. **--color Purple** should still report error but
1. **--color Purple --force** should accept this color as well.



## Exercise: Improve the Number Guessing game
{id: exercise-number-guessing-game-2}


Let the user guess several times (with responses each time) till he finds
the hidden number. Base your code on the solution from the previous exercise.
( examples/scalars/number_guessing.pl )



```
Allow the user to type
n   - skip this game and start a new one (generate new number to guess)
s   - show the hidden value (cheat)
d   - debug mode 
      (It is a toggle. 
       Pressing once the system starts to show the current
       number to guess every time before asking the user for new input
       pressing again, turns off the behavior.
       )
m   - move mode
      (It is a toggle.
       Pressing once the object will start to move a little bit after
       every step. Pressing again will turn this feature off.)
x   - exit
```


Now I can tell you that what you have is actually a 1 dimensional space fight
and you are trying to guess the distance of the enemy space ship.
As it is not a sitting duck, after every shot the spaceship can randomly move +2-2.





<emp>Extra exercise:</emp>



* For training purposes you might want to limit the outer space to 0-100.
* Make sure the enemy does not wander off the training field.
* Give warning if the user shoots out of space.
* Keep track of the minimum and maximum number of hits (in a file).




## Solution: improved color selector
{id: solution-color-selector}
![](examples/arrays/color_selector.pl)


## Solution: Improve the Number Guessing game
{id: solution-number-guessing-game-2}
![](examples/arrays/number_guessing.pl)




