# Perl References
{id: perl-references}


## References
{id: references}

```
    \$x    # reference to scalar
    \@y    # reference to array
    \%z    # reference to hash
    \&amp;f    # reference to function
```


## Passing values to a function
{id: simple-function}


Let's see a simple example of passing values to a function.


![](examples/references/add.pl)



## Add two (or more) arrays
{id: add-two-arrays-problem}
{i: @_}

```
Let's extend it so it will be able to take two vectors (arrays) and add
them pair-wise.  (2, 3) + (7, 8, 5) =  (9, 11, 5)
```

```
my @first  = (2, 3);
my @second = (7, 8, 5);
add(@first, @second);
```

```
The problem is, @_ in the add function will get (2, 3, 7, 8, 5);
We cannot know where does the first array end and where the second begins.

(I am sure one can come up with a complex way of prefixing the real data
by meta information that describes the data, but why work so hard if Perl
already has the tools you need?)
```


## Array References
{id: array-references}
{i: \@array}
{i: ARRAY}


To solve the problem we will use references.
Prefixing the array with a back-slash \ creates
a reference to it.



```
my $names_ref  = \@names;
```

```
print $names_ref;      # ARRAY(0x703dcf2)
```

```
@$names_ref
```


but it will be probably more readable to write



```
@{$names_ref}
```



or even




```
@{ $names_ref }
```



Once we know all this we can pass a reference to a function,
within the function we can dereference the array and we
get back the original array.


![](examples/references/array_references.pl)


[Passing two arrays to a function](https://perlmaven.com/passing-two-arrays-to-a-function)


## Add two arrays
{id: add-two-arrays}
![](examples/references/add_arrays.pl)


## Array References
{id: array-references-2}


Of course if the arrays are big, copying them is waste of time
and memory. Let's see how can we access the individual elements of
an array when using a reference to that array. Then we won't have
to copy them within the function.



```
my $names_ref = \@names;
```



<table>
<tr><td>Array</td>      <td>Array Reference</td></tr>
<tr><td>@names</td>     <td>@{ $names_ref }</td></tr>
<tr><td>$names[0]</td>  <td>${ $names_ref }[0]</td></tr>
<tr><td></td>           <td>$names_ref->[0]</td></tr>
<tr><td>$#names</td>    <td>$#$names_ref</td></tr>
</table>
You really don't want to use this $#$names_ref among people...





## Process arrays without copying
{id: array-ref-no-copy}


This is similar to the previous solution but without copying
the arrays


![](examples/references/add_arrays_nocopy.pl)


## Scope of variables
{id: scope-of-variables}
{i: scope}


Let's see an example where we create an array and a reference 
to it in some arbitrary {} scope. The array is defined within
the scope while the variable holding the reference is defined
outside the scope.



```
my $names_ref;
{
    my @names = qw(Foo Bar);
    $names_ref = \@names;
}
print "$names_ref->[0]\n"; # Foo

```

```
After the closing } @names went out of scope already
but $names_ref still lets us access the values.

As $names_ref still holds the reference to the location
of the original array in the memory perl keeps the content
of the array intact.
```


## Reference counting
{id: reference-counting}
{i: reference counting}


As you already know perl automatically allocates memory
when you add a new element to an array or hash. It also
frees up memory (although only internally) when you
remove the element from the array or hash.




Similarly when you create an array or a hash, perl sets up a
counter (called reference counter) and sets it to 1.
When the array or hash goes out of scope the counter is reduced 
by 1. If the counter reaches 0 perl frees the memory allocated 
to that array. Without references this is always the case.




When you create a reference to an array and store
it in a variable perl increases the reference counter of
the original array by 1 (to 2). Now if the array goes 
out of scope and the ref count is reduced by 1 it still does
not reach 0 so perl does not free up the location of the array.




Only if the reference stops referring to this memory location
will the counter reach 0 thereby freeing up the memory allocated
to the array.




## More Reference Counting
{id: more-reference-counting}

```
my @names     = qw(Foo Bar Baz);   # cnt = 1
my $names_ref = \@names;           # cnt = 2
my $other_ref = \@names;           # cnt = 3
my $x_ref     = $names_ref;        # cnt = 4

$other_ref = undef;            # cnt = 3
```



## Process arrays without copying even the return values
{id: array-ref-no-copy-return}


In the previous solution we passed the references to the function
but returned a full array, thereby copying all the values. If we 
care about memory and speed we might eliminate this copying by
returning the reference to the resulting array.




The cost is a small (?) inconvenience as now we have to dereference
the resulting array reference in the calling code.


![](examples/references/add_arrays_nocopy_return.pl)


## Hash References
{id: hash-references}
{i: \%hash}
{i: HASH}


Similarly to the Array references one can create references
to Hashes as well.



```
my $phones_ref = \%phones;
```


<table>
<tr><td>Hash</td>          <td>Hash Reference</td></tr>
<tr><td>%phones</td>       <td>%{ $phones_ref }</td></tr>
<tr><td>$phones{Foo}</td>  <td>${ $phones_ref }{Foo}</td></tr>
<tr><td></td>              <td>$phones_ref->{Foo}</td></tr>
<tr><td>keys %phones</td>  <td>keys %{ $phones_ref }</td></tr>
</table>




## Print out the content of a reference
{id: content-of-reference}


Using the print function to print out the content of an Array
was quite OK. Printing a Hash was a disaster. The same happens
once you dereference a reference to an array or hash.


![](examples/references/print_content.pl)


## Debugging (pretty printing)
{id: pretty-printing-references}
{i: Data::Dumper}


But once we have those references we have a better tool to print 
out their content.


![](examples/references/dump_content.pl)
![](examples/references/dump_content.out)


Actually you can use the Dumper on the references themself without 
putting them in scalar variables.



```
print Dumper \@names, \%phones;
```


## Change values in a reference
{id: change-value-in-reference}


If you create a copy of an array then the two arrays are separated.
Change to any of the arrays is not reflected in the other array.


![](examples/references/copy_array.pl)


When you create a reference to an array, then the referenced array
has the same memory location, hence change in either one of them
is  a change in both of them.


![](examples/references/change_reference.pl)


That means you can pass to a function an array reference, 
then from within the function it is easy to change the content of 
the original array.




## Exercise: double numbers
{id: exercise-double-numbers}


Create a function that gets an array reference and
multiplies each value in it by 2;



```
my @numbers = (2, 4, 7);
multiply_by_two(\@numbers);
print "@numbers\n";   # 4 8 14
```


## Exercise: Add many arrays
{id: exercise-add-many-arrays}


Pick up the examples/references/add_arrays.pl script that
can add two arrays and change it to accept any number of
array references.




Extra exercise: add parameters that will control to stop
the addition at the shortest array or the longest array.



```
my @a = (2, 3);
my @b = (4, 5, 6);
add('shortest', \@a, \@b); # returns (6, 8)
add('longest', \@a, \@b);  # returns (6, 8, 6)
```


## Exercise: Function to compare two hashes
{id: exercise-compare-hashes}


Create a function that given two hashes, returns a 
report showing missing keys or keys with different values.


![](examples/references/compare_hashes_skeleton.pl)
![](examples/references/compare_hashes.out)


## Solution: Double numbers
{id: solution-double-numbers}
![](examples/references/double_numbers.pl)


## Solution: Add many arrays
{id: add-many-arrays-recursive}
![](examples/references/add_many_arrays_recursive.pl)


## Solution: Add many arrays
{id: add-many-arrays}
![](examples/references/add_many_arrays.pl)


## Solution: Function to compare two hashes
{id: compare-hashes}
![](examples/references/compare_hashes.pl)


## Anonymous Arrays
{id: anonymous-arrays}
{i: anonymous array}
{i: []}


Occasionally we are not interested in the array @names, 
just in a reference to it. We can use the scoping trick
we saw earlier to force the array out of scope 
immediately once it was used.



```
my $names_ref;
{
    my @names     = ("Foo", "Bar", "Baz");
    $names_ref = \@names;
}
# @names is not in scope here
# $names_ref is still is
```


We can reach the same result without the temporary array and the
whole scoping issue by creating what we call an "anonymous array".
That is an array that does not have a real name, (@name) just a
reference to it.



```
my $other_names_ref = ["Foo", "Bar", "Baz"];

my $yet_another_names_ref = [ qw(Foo Bar Baz) ];
```


We got used to seeing [] as an indicator of an array element. The same visual
clue will help us remember that the above creates an array reference.




## Array of Arrays
{id: array-of-arrays}
{i: AoA}
![](examples/references/array_of_arrays.pl)


That already looks like a two dimensional array. 
It is not, but it can be used like one.





## Array of Arrays (AoA)
{id: anonymous-array-of-arrays}


Instead of naming the internal array references we can use 
them within the creation of the larger array.


![](examples/references/array_of_arrays_notemp.pl)


## Many dimensional arrays
{id: many-dimensional-arrays}
![](examples/references/many_dimensional_array.pl)
![](examples/references/many_dimensional_array.out)


## Anonymous hashes
{id: anonymous-hashes}
{i: anonymous hash}
{i: {}}
{i: HoH}
![](examples/references/anonymous_hash.pl)


## Hash of Hashes (HoH)
{id: hash-of-hashes}
![](examples/references/hash_of_hashes.pl)
![](examples/references/hash_of_hashes.out)


## More complex data structures
{id: complex-data-structures}

```
$grade{Name}{Subject}[index] = Exam-Grade;
$grade{Name}{Subject} = Final-Grade;
```
![](examples/references/complex_data_structure.pl)
![](examples/references/complex_data_structure.out)


## Memory leak with cross references
{id: memory-leak}
![](examples/references/memory_leak.pl)
![](examples/references/memory_leak.out)

{aside}

Run the script and when it displays the prompt, check the memory usage.
Passing 100,000 on the command line made it use 39 Mb memory.
{/aside}


## Memory leak with cross references - weaken
{id: memory-leak-weaken}
{i: weaken}
![](examples/references/memory_leak_weaken.pl)


## Read CSV file
{id: read-csv-file}
{i: CSV}
![](examples/references/data.csv)

```
We would like to read in that file and be able to access the fname of row 5
as  $data[3]{fname}

# the fname on line 5 is in index 3 because: 
# line 1 is the header
# line 2 is element 0 in the array
# ...
# line 5 is element 3 in the array
```
![](examples/references/read_csv_file.pl)
![](examples/references/read_csv_file.out)


## Exercise: read in an ini file
{id: exercise-ini-reader}

```
Read in an ini file and create a two dimensional hash.
First dimension - section name. Second dimension - key name.
print $data{Colors}{blue};   # dark
```
![](examples/references/data.ini)


## Exercise: improve the csv reader
{id: exercise-csv-reader}

```
Instead of an array create a hash in which the key is
the fname and the value is the hash reference.

To get the phone of 'Foo' we could write:

$data{Foo}{phone}
```

* First you can assume fname values are unique.
* Then improve it by checking if the fname is indeed unique and warn if not.
* Further improve it by removing the fname from the internal hashes.
* Further improve by passing the name of the key field (currently fname) as a parameter.
* Bonus: try to deal with the case when there are duplicate values for the key field without just giving an error message.



## Solution: Read ini file
{id: solution-ini-reader}


Read in an ini-file and create a two dimensional hash.


![](examples/references/read_ini_file.pl)


## Solution: improve the csv reader
{id: solution-csv-reader}
![](examples/references/read_csv_file_hash.pl)


## autovivification
{id: autovivification}
{i: autovivification}
![](examples/references/autovivification.pl)

Output:

![](examples/references/autovivification.out)


[What is autovivification?](https://perlmaven.com/autovivification)


## Scalar references
{id: scalar-references}
{i: scalar references}
{i: Getopt::Long}


Similar to array references and hash references one can also
create references to scalars.



```
my $name = "Foo";
my $name_ref = \$name;
```


It is used less often than the other references but one of the prominent
uses is the GetOptions function of Getopt::Long.



```
use Getopt::Long;
my $file = "default.txt";
my $debug;
GetOptions(
        "file=s" => \$file,
        "debug"  => \$debug,
) or die;
```


## Subroutine references
{id: subroutine-references}
{i: subroutine references}
{i: function references}
![](examples/references/sub_ref.pl)


## Anonymous subroutines
{id: anonymous-subroutine}
![](examples/references/anon_sub.pl)



## Uses of Subroutine references
{id: uses-of-subroutine-references}


The find() function of File::Find.




## Exercise: DNA Sequence Analyzer
{id: exercise-dna-sequence-analyzer}


Create a function for researching DNA sequences. Below, you can see the "source" file.
There is all kind of extra information, that is currently not interesting to us.
Implement the read_file function that goes over the given file extracting and returning the list
of all the DNA sequences. The user of your function can now, create a foreach-loop going over
the list of DNA sequences and call her own function that will analyze the sequence
and print the results. See the input file, the skeleton of the solution in which I already
added the analyze function the end user is going to write. The expected output can be also found.
(Of course this read_file should work regardless of what the analyze function does.)


![](examples/references/dna.txt)
![](examples/references/dna1_skeleton.pl)
![](examples/references/dna.out)


## Solution: DNA Sequence Analyzer
{id: solution-dna-sequence-analyzer}
![](examples/references/dna1_solution.pl)


## Exercise: DNA Sequence Analyzer with callback
{id: exercise-dna-sequence-analyzer-callback}


The above can work, but if the file is huge, we might not be able to hold all the list in memory.
Change the read_file function that to allow the user to supply the analyze function
(or rather the reference to the analyze function) as a parameter. See the skeleton below.
The output should be the same as above.


![](examples/references/dna2_skeleton.pl)


## Solution: DNA Sequence Analyzer with callback
{id: solution-dna-sequence-analyzer-callback}
![](examples/references/dna2_solution.pl)


## Exercise: DNA Sequence Analyzer with shortcut
{id: exercise-dna-sequence-analyzer-shortcut}


What if you would like to provide the user the ability to stop
the processing any time she wants even if the file has not finished yet?
For example when she found the first match. This can be controlled
by the return value of the analyze function. If it is true, stop processing.
See the skeleton and the expected output: 


![](examples/references/dna3_skeleton.pl)
![](examples/references/dna3.out)


## Solution: DNA Sequence Analyzer with shortcut
{id: solution-dna-sequence-analyzer-shortuct}
![](examples/references/dna3_solution.pl)


## Dispatch Table
{id: dispatch-table}
![](examples/references/dispatch_table.pl)


## Dispatch Table using symbolic references
{id: dispatch-table-symbolic-reference}
![](examples/references/dispatch_table_symref.pl)


## The ref() function
{id: ref-function}
{i: ref}

```
my $name = 'Foo';
ref($name);           # undef
ref(\$name);          # SCALAR
my $array_ref = [];
ref($array_ref);      # ARRAY
my $hash_ref = {};
ref($hash_ref);       # HASH
my $sub_ref = sub {};
ref($sub_ref);        # CODE
```


## Copy a data structure
{id: copy-data-structure}

```
Copy an array or hash referred to by a reference.
```
![](examples/references/copy_array_ref.pl)

```
Copy HASH reference
$other_phones_ref = { %{$phones_ref} };
```


## Deep copy
{id: deep-copy}
{i: deep copy}
![](examples/references/deep_copy.pl)
![](examples/references/deep_copy.out)


## Deep copy - Storable dclone
{id: deep-copy-dclone}
{i: dclone}
![](examples/references/deep_copy_dclone.pl)


## Serialization
{id: serialization}
{i: Data::Dumper}
{i: Storable}
{i: YAML}
{i: JSON}
{i: XML::Dumper}

* [Data::Dumper](http://metacpan.org/pod/Data::Dumper)
* [Storable](http://metacpan.org/pod/Storable)
* [YAML](http://metacpan.org/pod/YAML)
* [JSON](http://metacpan.org/pod/JSON)
* [XML::Dumper](http://metacpan.org/pod/XML::Dumper)



## Data::Dumper
{id: data-dumper}
![](examples/references/data_dumper_dump.pl)
![](examples/references/data_dumper_dump.dump)
![](examples/references/data_dumper_restore.pl)


## Data::Dumper both dump and restore
{id: data-dumper-dump-and-restore}
![](examples/references/data_dumper.pl)


## Storable
{id: storable}
![](examples/references/storable_store.pl)


creates a binary file


![](examples/references/storable_retrieve.pl)


## Storable in memory freezing
{id: storable-in-memory}
![](examples/references/storable_freeze_thaw.pl)


## YAML
{id: yaml-dump-load}
![](examples/references/yaml.yml)
![](examples/references/yaml_dump.pl)
![](examples/references/yaml_load.pl)


## YAML in one file
{id: yaml}
![](examples/references/yaml.pl)


## JSON in one file
{id: json}
![](examples/references/json.out)
![](examples/references/json.pl)


## Main uses of references
{id: use-of-references}

* Creating complex data structure (2 or more dimensional arrays, hashes and more complex structures)
* Passing arrays, hashes and more complex data structure to and from functions 



## Exercise: save ini and csv as YAML
{id: exercise-yaml}

```
Take the ini-file reader and the csv reader and save the resulting data
structures in YAML format.
```


## Exercise: Create a cache for NetSlow
{id: exercise-netslow}

```
You are using a module call NetSlow.pm and its sole function compute();
This function can get two numbers and after a remote procedure call
(that takes a lot of time) returns a single value. Create a local cache
of the given input values and results so you won't need to access the
remote machine for identical calls. (Make sure your cache is persistent
between execution of your script.

examples/references/NetSlow.pm

Here is how we can use the module: 
```
![](examples/references/netslow.pl)


```
Later on you find out that the results are changing over time.
You don't want to drop the caching and you decide you can live with
certain lack of accuracy. You decide you fetch the value again if 
the last call to that specific set of input values was computed more 
than 5 seconds ago. That is you expire the cache after 5 seconds.
```


## Exercise: create a function that generates numbers multipliers
{id: exercise-multiply-numbers}


Create a function that given a number returns a subroutine reference.
Calling that subroutine with an array reference will then multiply each
value by the originally given number.



```
my $duplicate = multiplier_generator(2);

my @numbers = (2, 4, 7);
$duplicate->(\@numbers);
print "@numbers\n";   # 4 8 14
```


## Solution: save ini and csv as YAML
{id: solution-yaml}

```
Just add the following code:
```

```
use YAML qw(DumFile);
DumpFile 'ini.yml', \@data; # in read_csv_file_hash.pl

DumpFile 'ini.yml', \%ini; # in read_ini_file.pl

DumpFile 'csv.yml', \%data; # in read_csv_file_hash.pl
```


## Solution: Create a cache for NetSlow
{id: solution-netslow}
![](examples/references/netslow_cache.pl)


## Solution: NetSlow cache with timeout
{id: solution-netslow-timeout}
![](examples/references/netslow_cache_timeout.pl)


## Resources
{id: references-resources}


Perl documentation:



* perlreftut - Mark Jason Dominus's very short tutorial about references
* perllol - Arrays of Arrays
* perldsc - Data Structure Cookbook
* perlref - Perl references and nested data structures
* perldata - Perl data types



Books:
</p> 

* Perl Objects, References &amp; Modules (Intermediate Perl)
* Advanced Perl Programming 1st edition !
* Object Oriented Perl





