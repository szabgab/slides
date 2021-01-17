# Basic Testing Framework in Perl
{id: test-module}

## Things we are going to test
{id: testing-plan}

* Test a module
* Test complex Perl applications
* Test any application

{aside}
As an introduction to testing with Perl, first we are going to write
unit tests for a simple Perl module.

From there, we'll be able to move on to test more complex applications
written in Perl. Then to test any application no matter in what
language it is written in.
{/aside}

## Testing a simple Perl module
{id: test-scripts}

{aside}
We have a module called MySimpleCalc.pm with a single function called sum().
It is supposed to return the sum of numbers passed to it.
{/aside}

![](examples/test-simple/lib/MySimpleCalc.pm)

* sum(1, 3)

## Calculator test
{id: test-calculator}

{aside}
How would you make sure this function works correctly?
You'd probably write a small, temporary script to call the function with various
sets of input and you'd then check if the results are as expected.
{/aside}

{aside}

Let's do that. Write a script using the sum() function of the module and printing the results.
{/aside}

![](examples/test-simple/tests/t01.pl)

{aside}

In this script we use the $Bin variable of the FindBin module to let perl find the MyTools.pm file.
{/aside}

If you run this script, the output will look like this:

![](examples/test-simple/tests/t01.pl.out)


There was an error on the last line. 2 + 2 + 2 should be 6 and not 4


{aside}
After some further experimenting we find out that the
problem seems to be, that sum() does not handle more than
2 parameters.

While this is a very simple example, it is easy to overlook the simple
detail, not noticing that one of the results was indeed incorrect.

Of course this is a simple computation and anyone should know
what is the expected result, but what if we are testing something more complex?

Do you know what should be the result? Will you compute it every time
manually to check if that's the correct answer?
{/aside}

{aside}
We could fix the code, but we will use this case to show how to write tests.

At this point we are not interested in fixing the bug in MyTools.pm.
We are interested in a robust way to write tests for it.

We'll use this example but we have not solved our biggest problems yet:

We cannot expect our test engineers looking at the results to know
the valid result of each line.
{/aside}



## Test with expected results
{id: test-with-expected-results}

{aside}

We should write the expected value next to the actual result:

In order to make it obvious what are the expected values first we have to compute
them ourself - or bring in the expert, or the client who knows what she expects
from the application to display - and make sure the expected values are always written
next to the actual results.

That way it will be obvious to any tester what values need to be compared.
{/aside}
![](examples/test-simple/tests/t03.pl)


Output:

![](examples/test-simple/tests/t03.pl.out)

Now it is better.


## More test cases, more output
{id: more-output}

{aside}
Still, if the output is more complex than a single, short number,
or if there are many results, it will be difficult
to the person comparing to notice the differences.

What if we have 100s of test cases?
{/aside}

![](examples/test-simple/tests/t04.pl)

Output:

![](examples/test-simple/tests/t04.pl.out)


## Complex output
{id: complex-output}

```
qwertyuiopasdfghjklmnopqrs qwertyuiopasdfghjk1mnopqrs
```

{aside}
It would be much better if our testing program already compared the expected value
with the actual results and would only print "ok" or "not ok"
depending on success or failure.

Like this:
{/aside}


## ok, not ok
{id: ok-not-ok}

```
ok
ok
not ok
ok
ok
ok
ok
ok
```


## Print only ok/not ok
{id: print-only-ok}

{aside}
Good so we are going to implement that now. For every test unit we
create an if statement that will print either "ok" or "not ok"
depending on the result.
{/aside}

![](examples/test-simple/tests/t05.pl)


Output:


![](examples/test-simple/tests/t05.pl.out)


The output is as we expected. I mean we already know there is a bug somewhere.
We are supposed to report it to the developers, but right now we are focusing on improving our
test suite and its reporting capabilities.


## Refactor - Write the ok function
{id: ok-function}
{i: ok}

{aside}
As we are not only testers but also developers we quickly notice the
repeating pattern and decide to move it to a function so we will write
less code. As we would like to be short, we call the function
**ok()**. As we'll see we are not the only ones who want to
type as little as possible.
{/aside}

{aside}
This ok() function gets a "true" or "false" value
(that is the result of a comparison such as == in our examples.)
{/aside}

{aside}
Reminder: In Perl undef, 0, "" and "0" count as false and all other
values as true.
{/aside}

![](examples/test-simple/tests/t06.pl)

Output:

![](examples/test-simple/tests/t06.pl.out)

But why reinvent the wheel ?


## Introducing Test::Simple
{id: introducing-test-simple}
{i: Test::Simple}

{aside}

The Perl community has already created several implementations
of the above mentioned ok() function. We'll go with the one in the module called
Test::Simple. Not only will that print "ok" or "not ok" but it will also
include a counter.

In order to use it first we'll need to declare how many test units are we planning
to call, that is, how many times are we planning to call the ok() function.

In return we get extra features such as printing the line numbers of the ok() calls
that failed and getting a final report on the number of failed tests out of the
planned tests.

use Test::Simple, tell it your **plan**, that is the number
of times you are going to call **ok()** and use its built in ok()
function.
{/aside}

![](examples/test-simple/tests/t10.pl)


Output:

![](examples/test-simple/tests/t10.pl.out)

{aside}
It is more verbose, it has a couple of additional useful pieces of information:
1..3   says how many tests we were planning,
then we get the tests numbered and we even get a small explanation when the test fails.
{/aside}

```
$ echo $?
1
```

```
> echo %ERRORLEVEL%
1
```

## Test::Simple when everything is ok
{id: introducing-test-simple-everything-is-ok}

{aside}

For the following example we've replaced the failing test with one that is successful.
This way you can see how does it look like when everything is ok.
{/aside}

![](examples/test-simple/tests/t11.pl)

Output:

![](examples/test-simple/tests/t11.pl.out)

```
$ echo $?
0
```

```
> echo %ERRORLEVEL%
0
```


## Test::Simple - missing test
{id: introducing-test-simple-missing-test}
{i: count}

{aside}

So why are those numbers necessary?
Imagine you managed to write 200 unit tests. Someone
who does not know about the number runs the test suite and
sees "ok" printed 17 times. It looks like everything is ok. He won't notice
that instead of 200, only 17 tests ran before the test script excited.
Everything was OK up to that point,
but there is a serious problem somewhere. Either in the
application or in the test itself. This can be found only
if the test executer knows how many test have you planned,
and checks if the correct number of tests have been executed.
{/aside}

{aside}
This is exactly what Test::Simple provides. In the following example
we deliberately commented out the last test that was failing.
{/aside}

![](examples/test-simple/tests/t12.pl)

Output:

![](examples/test-simple/tests/t12.pl.out)

```
$ echo $?
255
```

```
> echo %ERRORLEVEL%
255
```


## Test::Simple - too many tests
{id: test-simple-too-many-tests}


When there are more OKs than planned the script will also print a comment about it.

![](examples/test-simple/tests/t13.pl)

Output:

![](examples/test-simple/tests/t13.pl.out)

```
$ echo $?
255
```

```
> echo %ERRORLEVEL%
255
```


## Add names to the tests
{id: test-names}
{i: names}

```
More advantages of Test::Simple - names of the tests.
```

{aside}
So Test::Simple module makes our life a bit more simple in that we don't have to write
our testing expression. In addition this new "ok" function can actually do some more.
It can get two arguments. The first one indicates success or failure of the test
as explained earlier. The second one is a string which is the name of the test.
When running a test these additional names get printed on the same
line where the counter and the "ok" or "not ok" is printed.
If the names were written carefully, then they can provide an immediate hint on what went wrong.
Sometimes you won't even need to look at the test script itself, right from this comment
you'll know where to look for the bug.
{/aside}

![](examples/test-simple/tests/t14.pl)

Output:

![](examples/test-simple/tests/t14.pl.out)

## Exercise: Write tests for fibo
{id: exercise-tets-fibo}

Given the following module test the `fibo()` function that returns the values of the [Fibonacci series](https://en.wikipedia.org/wiki/Fibonacci_number).

![](examples/test-simple/lib/MyFibo.pm)

## Exercise: Write a test to test the Anagram checker
{id: exercise-anagrams}

* [Anagrams](https://en.wikipedia.org/wiki/Anagram) are words with the exact same letter, but in different order.
* silent - listen

![](examples/test-simple/lib/MyAnagram.pm)

## Exercise: Enlarge the test
{id: exercise-enlarge-test-suit}

Take the test file from the last example ( examples/test-simple/tests/t14.pl ) and add a few more tests.

## Solution: Write tests for fibo
{id: solution-tets-fibo}

![](examples/test-simple/tests/fibo.pl)
![](examples/test-simple/tests/fibo.out)

## Solution: Write a test to test the Anagram checker
{id: solution-anagrams}

![](examples/test-simple/tests/anagram.pl)
![](examples/test-simple/tests/anagram.out)

## Solution: Enlarge our test suite
{id: solution-enlarge-test-suit}

![](examples/test-simple/tests/t20.pl)

Output:

![](examples/test-simple/tests/t20.pl.out)

## Refactor larger test suite
{id: refactor-large-test-suit}

{aside}
Now that we have this tool in place it is time to start to enlarge our test suite.
After all three tests are not enough. As we are adding more and more tests we can
recognize again that there is the data part of the tests that are changing and the
code part which is repeating. This is a good time to refactor our code again.
We take the data and move it to a data structure. The code then can go over this
data structure and execute each unit on its own.
{/aside}

![](examples/test-simple/tests/t21.pl)

Output:

![](examples/test-simple/tests/t21.pl.out)

{aside}

For every unit we created an array reference where the last element is the expected
output. Anything before that is the list of parameters.
We then created an array (@tests) of all these units.
{/aside}

{aside}

In the code we loop over all the units, $t holding the current unit,
and then extract the expected output using pop.
The remaining values are the parameters to the test.
We also generate the name of the test from the input values.
{/aside}

{aside}

There is a small problem though.
When you add a new test to the array, you also have to remember to update the
tests => 6 line.

There are a number of solution to this problem
{/aside}


## Forget about your "plan", use "no_plan"
{id: no-plan}
{i: plan}
{i: no_plan}

![](examples/test-simple/tests/t22.pl)

Output:

![](examples/test-simple/tests/t22.pl.out)


The 1..6 is now at the end.



{aside}

This is one of the solutions and in some cases it is hard to avoid it,
but it is not a really good solution. Those who advocate never to put
'no_plan' in your test say that checking if the exact number of unit
tests were executed is an additional control over our test suite.
Without a 'plan' you can never be sure if - after a successful execution -
the OKs you see were all the units there, or if the test script aborted
in the middle and you have not executed all of the units.

There are also people who say it is not that important to have a plan but
personally I am in the first camp. I think the plan is important.
{/aside}

{aside}

There is 'done_testing' we'll cover later on.
{/aside}


## use BEGIN block with Test::Simple
{id: begin-test-simple}
{i: BEGIN}

{aside}
Another solution is the use of BEGIN blocks. In case you don't know, code that is placed in a
BEGIN block will be executed as soon as it gets compiled. Even before the rest of the code gets compiled.

So in the next example the array @tests will already have content when perl tries to compile the "use Test::Simple ..."
statement. This way "scalar @tests" will already return the number of elements in the array.

Please note, we have to declare "my @tests" outside the BEGIN block or it will be scoped inside that block.

This is a good solution, though it requires the use of BEGIN, which might be considered as somewhat advanced feature of Perl.
{/aside}

![](examples/test-simple/tests/t23.pl)

Output:

![](examples/test-simple/tests/t23.pl.out)


## Put the test cases in an external file
{id: test-case-in-external-file}

{aside}
By now we almost totally separated the data of the tests in the array from the code that executes the test, but we can go a bit further.

We can move the test data to some external file. Let's create a text file that looks like the following file:

Here each line is a test-case. On the left side of the = sign are the parameters of the sum() function, on the right hand side of the =
is the expected result.

We even allow for empty rows and comments: rows that start with a # character will be disregarded.
{/aside}

![](examples/test-simple/tests/sum.txt)

{aside}

Instead of having the data in the BEGIN block, we put code in there that will read the data file line-by-line.
It skips the lines that are either empty or contain only comments.
Lines that contain data are split at every comma and the = sign. Spaces around the signs are removed. The array we get
(@data) contains the information for one test-case. We push the reference to that array on the @tests array.
This way, by the end of the BEGIN block the @tests array will look exactly as it looked in the previous example.

The code outside the BEGIN block stays the same.
{/aside}

![](examples/test-simple/tests/t24.pl)

Output:

![](examples/test-simple/tests/t24.pl.out)

{aside}
If for some reason the sum.txt file cannot be opened, we'll get an error message like this:
{/aside}

```
Could not open '.../sum.txt': No such file or directory at t24.pl line 11.
BEGIN failed--compilation aborted at t24.pl line 18.
```

## Large test suite
{id: large-test-suit}

![](examples/test-simple/tests/large_sum.txt)

```
$ cp tests/large_sum.txt tests/sum.txt

$ perl tests/t24.pl
```


## Harness
{id: test-harness}
{i: harness}
{i: Test::Harness}

{aside}
This is a module that can analyze the ok / not ok printouts with the numbers.
In particular, it can analyze the output of Test::Simple and a whole class of
other modules in the Test::* namespace on CPAN we are going to see later.

The harness.pl script is just a sample usage of the Test::Harness module.
It accepts one or more test files, runs them and analyzes the output they generated.
{/aside}

![](examples/root/harness.pl)


Run the previous test file using Test::Harness


```
$ perl ../root/harness.pl tests/t24.pl
```

{aside}
If the original test script had very few test units then this output won't make much sense, but if the original
test script had hundreds of OKs, we would not be really interested on all those OKs. We would be mainly interested
in a summary, and in the (hopefully) little number of "NOT OK" printouts. This is how the output of Test::Harness looks like:
{/aside}

![](examples/test-simple/tests/large_harness.out)

## Harness on success
{id: harness-on-success}

{aside}
In the case when all the OKs were successful the output is much shorter:
{/aside}

```
$ perl ../root/harness.pl tests/t11.pl
```

![](examples/test-simple/tests/harness_t11.out)


## Harness on too few tests
{id: harness-on-too-few-tests}

```
$ perl ../root/harness.pl tests/t12.pl
```

![](examples/test-simple/tests/harness_t12.out)


## prove
{id: prove}
{i: prove}

```
prove tests/t24.pl
prove tests/t11.pl
prove tests/t12.pl
```

## Packaging as people do for CPAN
{id: packaging-cpan-modules}
{i: CPAN}

{aside}
Now let's take a small journey into how people package modules that
are on CPAN. I have been using this method for all my code whether
it was open source and ended upon CPAN, or a web application that
I am only developing for myself, or code for a client.
{/aside}

{aside}
If you are packaging your application in the same way as all the
CPAN modules are packaged, you'll immediately get all kinds of nice
features other Perl developers have built for themself.
So let's see how they are doing it.
There are three major ways how to package a module for CPAN.
We could call them "standards" but it is quite hard to talk about
standards in the Perl world.
{/aside}

{aside}
The three tools are three Perl Modules: ExtUtils::MakeMaker,
Module::Build and Module::Install. Out of these three
ExtUtils::MakeMaker has been standard for ages. Module::Build is
standard from 5.10 and Module::Install actually builds on
ExtUtils::MakeMaker and it packages itself with your distribution
so it does not have to be installed on the target system.
{/aside}

{aside}
The major advantage of Module::Build is that if you are writing
pure perl modules you only need to know about Perl. If you are
writing some code that is partially written in C and requires
compilation then you'll probably have to know about Makefiles
anyway so there might not be any advantage to using Module::Build.
{/aside}

{aside}
When using Module::Build you are going to create a file called
Build.PL that describes the installation process while for
ExtUtils::MakeMaker and Module::Install you need to prepare
a file called Makefile.PL.
{/aside}

{aside}
A CPAN distribution has the following directory layout.
In the root directory of the distribution there is the Makefile.PL
or Build.PL or sometimes both. The README file is not a
requirement but it is nice to have a short explanation of what
the module is and how to install it. Especially if the installation
is not fully automated or if there are special prerequisites.
{/aside}

{aside}
The CHANGES or Changes files is another nice to have file. People
usually include the major changes between version in that file so
the user can easily see what is in the new version or to see the
history of releases.
{/aside}

{aside}
For testing purposes you don't need MANIFEST, but if you plan to
distribute your code even internally in your company, it is an
important and required file. The MANIFEST file contains a list
of all the files included in the distribution.
On one hand the standard tools use this list to know what to
include on the other hand when opening the distributed zip file
this is the file that helps to check if all the necessary files
have arrived. I think it is important to manually update this
file as we add and remove files from our code but the Perl
community is divided on the issue. Some people like me keep
the file in version control and manually update it when necessary
using it as a control mechanism. Others keep a file called
MANIFEST.SKIP that lists all the files that are not to be
included in the MANIFEST and then autogenerate the MANIFEST file.
Some don't even have a MANIFEST.SKIP, they just make sure that
there is no extra file in the directory when they release a new
version so they can just include everything in MANIFEST and
thus in the distributions.
{/aside}

{aside}
META.yml is a file in YAML format that contains machine readable
meta-data about the projects. This meta data contains the name
and the version of the module, list of prerequisites, license
information and a lot of other data. Most of the people
autogenerate this file with.
{/aside}

{aside}
In addition to these files the modules that are provided by this
package can be found in the lib subdirectory. In case there are
also scripts to be installed, they are either in a directory called
bin, or in a directory called scripts.
{/aside}

{aside}
The t/ directory holds all the test files with a .t extension.
{/aside}

```
Directory layout

  Makefile.PL
  Build.PL
  dist.ini

  README
  CHANGES
  MANIFEST.SKIP
  MANIFEST             (generated)

  META.yml             (generated)
  META.json            (generated)
  MYMETA.yml           (generated)
  MYMETA.json          (generated)

  lib/                 Modules
  bin/                 scripts
  t/                   test scripts with .t extension
```

* ExtUtils::MakeMaker  Makefile.PL
* Module::Install      Makefile.PL
* Module::Build        Build.PL
* Dist::Zilla          dist.ini


## Makefile.PL for ExtUtils::MakeMaker
{id: makefile-pl-extutils-makemaker}
{i: Makefile.PL}
{i: ExtUtils::MakeMaker}

![](examples/distribution/project_with_extutils_makemaker/Makefile.PL)

{aside}
In this example Makefile.PL we have to say what is the name of the
module, and in which file is the version number - this value will be
part of the generated filename. The LICENSE field is a relatively
new addition. In this example I am using the "perl" license
but if you are writing this for a company then you'll probably
use the word "restrictive".

Once you have setup the directory structure and created a simple
Makefile.PL you can type the following:
{/aside}

```
$ perl Makefile.PL
$ make
$ make test
```

{aside}
In Windows you'll probably have nmake or dmake instead of make.

In the above three steps "perl Makefile.PL" checks if all the
prerequisites are met and creates a Makefile.

make would compile your code if you had some C code in your
application and also copy all the files to a new "blib"
directory just in the project directory.

The most interesting for us is the third step:
make test will run all your .t file within the t/ directory
using Test::Harness. So you don't have to deal with it yourself
and anyone who is familiar with the standard hierarchy of Perl
modules will immediately know what to do.

In addition there are several other things you can do.
Most notably you can execute the following command, and
create the distribution you are supposed to upload to
CPAN or to give to your users.
{/aside}

```
$ make manifest
$ make dist
```


## Makefile.PL for Module::Install
{id: makefile-pl-module-install}
{i: Makefile.PL}
{i: Module::Install}

![](examples/distribution/project_with_module_install/Makefile.PL)

{aside}
In Module::Install the declaration is cleaner and it does not need to be
installed on the target machine. When running perl Makefile.PL it creates
and inc subdirectory and copies itself there. One should distribute
this directory as well.
{/aside}

{aside}
On the target system Module::Install is loaded from this subdirectory.
{/aside}

```
$ perl Makefile.PL
$ make
$ make test
```

```
$ make manifest
$ make dist
```


## Build.PL
{id: build-pl}
{i: Build.PL}

![](examples/distribution/project_with_module_build/Build.PL)

```
$ perl Build.PL
$ perl Build
$ perl Build test
```

```
$ perl Build manifest
$ perl Build dist
```



## Directories under t and prove
{id: test-more-prove}

```
t/
  other.t
  something.t
  win32/
       ui.t
```

```
prove                   t/*.t
prove -r                recursively
prove t/something.t     t/something.t
prove t/win32           t/win32/*.t
```

{aside}
If our test suite was setup as outlined above, even without a real perl module,
we can also keep the test files in a directory hierarchy under t/ - in that case we have
to indicate this in Makefile.PL or Build.PL. We can also run the tests script one-by-one
or per directory using the "prove" utility.
{/aside}

{aside}
Let's see the layout of the sample CPAN packages we have, and run their tests:
{/aside}

{aside}
By default "make test" or "perl Build test" will run all the t/*.t files.
Sometimes we want to run them one by one. We could run
**perl t/something.t** but that would try to use the installed
versions of the modules you are using and not those you are about to install.
So better use **perl -Ilib t/something.t** for that.

Even better to use the **prove t/something.t** command that comes with Test::More.
It too by default would attempt to use the already installed modules so you could run
**prove -b t/something.t** to include the files from blib/lib.
Prove has another frequently used flag: -v which puts it in verbose mode.
{/aside}

## Simple CPAN-like module
{id: simple-cpan-like-module}

```
.
├── Changes
├── lib
│   └── MyTools.pm
├── Makefile.PL
├── MANIFEST.SKIP
├── README
└── t
    └── 01-add.t
```

![](examples/distribution/project_with_extutils_makemaker/Changes)
![](examples/distribution/project_with_extutils_makemaker/Makefile.PL)
![](examples/distribution/project_with_extutils_makemaker/MANIFEST.SKIP)
![](examples/distribution/project_with_extutils_makemaker/README)

![](examples/distribution/project_with_extutils_makemaker/lib/MyTools.pm)
![](examples/distribution/project_with_extutils_makemaker/t/01-add.t)


## Exercise: Add tests
{id: exercise-test-simple-add-tests}

1. Add some tests to the `01-add.t` file.
1. Create a new file called 02-multiply.t` and add tests to verify the `multiply()` function.
1. See how it works when running directly with perl and using harness
1. Add a new entry to the
1. Run it using `make test`.

## Test::Simple
{id: test-simple}

```
This is all very nice and Simple.


What if you want More ?
```
