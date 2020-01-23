# Perl Libraries and Modules
{id: perl-modules}


## Lack of code reuse
{id: lack-of-code-reuse}

* common functions
* copy-paste
* Perl4 solution: create libraries


## Perl library (perl4 style)
{id: perl-library}

![](examples/modules/library.pl)
![](examples/modules/perl4_app.pl)

The 1; at the end of the library is needed in order to make sure the
compilation of library.pl returns a true value.

Otherwise one could get an error such as this one:

`examples/modules/library.pl` did not return a true value


## Problems with Libraries
{id: problems-with-libraries}

* All or nothing
* Potential collision (redefine)
* Global variables

While libraries can help in code reuse they still lack many features.


## Prefix everything with unique name
{id: prefix-everything}

![](examples/modules/calc_prefix_lib.pl)

But we always have to use this prefix. Even within the library.


## Namespaces
{id: perl-namespaces}

Perl has a solution to this problem using namespaces, also called packages.

![](examples/modules/namespaces.pl)


## Solution with namespace
{id: perl-namespace}

![](examples/modules/namespace.pl)
![](examples/modules/namespace_lib.pl)

Here, within the Calc namespace you don't have to use the full
name, only when you are using it outside.


## Modules
{id: modules}

We could have placed the package keyword and the code in the main script
or we can put several packages in the same external file but the
best approach is to put every package in a separate file having
the same name as the package itself (case sensitive)
and .pm as file extension.

Then we call it a Perl Module.

![](examples/modules/module.pl)
![](examples/modules/Calc.pm)

* How did perl find the file Calc.pm ?
* How could we use add() without the Calc:: ?
* Why did we write "require" instead of "use"?


## Packages, @INC and Namespace hierarchy
{id: packages-and-inc}

`perl -V`


```
@INC:
  C:/strawberry/perl/lib
  C:/strawberry/perl/site/lib
  C:\strawberry\perl\vendor\lib
  .
```

`require Calc;` - Calc.pm somewhere in @INC

`require Math::Calc;` - Math/Calc.pm somewhere in @INC

`require Math::Calc::Clever;` - Math/Calc/Clever.pm somewhere in @INC


## use, require and import
{id: use-require-import}

```
require Math::Calc;
```

```
use Math::Calc qw(add);
```

```
BEGIN {
    require Math::Calc;
    Math::Calc->import( qw(add) );
}
```


<command>use</command> is executed at compile time, just as a BEGIN block.
<command>require</command> is executed at run time so if we don't enclose it
in a BEGIN block it will happen later.



```
if ($holiday) {
    use Vaction::Mode;
}
```

The above does not make much sense as the <command>use</command> will load the module
at compile time regardless of day.



```
if ($holiday) {
    require Vacation::Mode;
    Vacation::Mode->import;
}
```


And we don't even need to call import() if we don't care about that.




## Export - Import
{id: perl-export-import}

```
In order to eliminate the need to use the full name of
a subroutine e.g. Calc::add() we can export it from the module
and the user can import it into the namespace of her own code.

(we call it A::Calc as we already had a Calc.pm in the previous slide)
```
![](examples/modules/calca.pl)
![](examples/modules/A/Calc.pm)

```
Exporter is a standard module that provides the 'import' function called by
'use Module' automatically.

This imports automatically every function (and variable) mentioned in the
@EXPORT array. This is nice as the user (the script writer) does not have
to think much.

On the other hand it might be bad as the user gets many functions she does not
need, just because the module author thinks these functions are useful.
```




## Restrict the import
{id: perl-restrict-import}

```
The user (the script writer) can restrict the list of imported
functions but the unsuspecting script write will still get all the functions.
```
![](examples/modules/calca_2.pl)


## On demand Import
{id: on-demand-import}
![](examples/modules/B/Calc.pm)
![](examples/modules/calcb.pl)




## Importing
{id: importing}

```
use Module;
```

```
Every function (and variable) listed in the @EXPORT array is imported
automatically.
```

```
use Module ();
```

```
Nothing is imported.
```

```
use Module qw(foo bar);
```


Functions foo() and bar() are imported, nothing else.
Any function from the @EXPORT and @EXPORT_OK arrays can be requested to be imported.
There is also an %EXPORT_TAGS that can be used to define groups of functions to be imported.




## Modules - behind the scene
{id: perl-modules-behind-the-scene}

* The functionality of Cwd is implemented in a file called Cwd.pm
* @INC    the list of libraries
* **perl -V**
* **perldoc Cwd** documentation
* **perldoc -l Cwd** location /usr/lib/perl5/5.8.6/i386-linux-thread-multi/Cwd.pm
* **perldoc -m Cwd** module content


```
Examples of modules that export functions. Look at their source code

- Cwd
- File::Basename
- File::Spec
- File::Spec::Functions
```


## Tools for packaging and distribution
{id: tools-for-distribution}

* [ExtUtils::MakeMaker](http://metacpan.org/pod/ExtUtils::MakeMaker)
* [Module::Build](http://metacpan.org/pod/Module::Build)
* [Module::Install](http://metacpan.org/pod/Module::Install)
* [Dist::Zilla](http://metacpan.org/pod/Dist::Zilla)


* [PAR](http://metacpan.org/pod/PAR)
* [PAR::Packer](http://metacpan.org/pod/PAR::Packer)



## Packaging modules
{id: packaging-modules}


The semi-standard directory structure of CPAN modules can be also very useful for any Perl application:



```
  dir/

     Makefile.PL
     Build.PL

     dist.ini


     README
     CHANGES
     MANIFEST
     MANIFEST.SKIP
     META.yml
     META.json

     lib/
        Application/Name.pm
        Application/Name/...
     script/
        application.pl

     t/
     xt/

     sample/

     share/
     templates/
     views/
```


## Makefile.PL of ExtUtils::MakeMaker
{id: packaging-module-example-extutils-makemaker}
![](examples/modules/app/Makefile.PL)


## Makefile.PL of Module::Install
{id: packaging-module-example-module-install}
![](examples/modules/app/Makefile2.PL)


## Build.PL of Module::Build
{id: packaging-module-example-module-build}
![](examples/modules/app/Build.PL)


## Changes and README
{id: packaging-module-example-changes-and-readme}
![](examples/modules/app/CHANGES)
![](examples/modules/app/README)


## MANIFEST and MANIFEST.SKIP
{id: packaging-module-example-manifest}
![](examples/modules/app/MANIFEST)
![](examples/modules/app/MANIFEST.SKIP)


## A script
{id: packaging-module-a-script}
![](examples/modules/app/script/app.pl)


## A module
{id: packaging-module-the-module}
![](examples/modules/app/lib/App.pm)


## Packaging with Makefile.PL
{id: packaging-module-running-makefile-pl}

```
perl Makefile.PL
make
make test
make manifest
make dist

When installing you'll have to type <command>make install</command>
instead of the <command>make manifest</command> and the <command>make dist</command>
```


## Packaging with Build.PL
{id: packaging-module-running-build-pl}

```
perl Build.PL
perl Build
perl Build test
perl Build manifest
perl Build dist

When installing you'll have to type <command>perl Build install</command>
instead of the <command>perl Build manifest</command> and the <command>perl Build dist</command>.
```


## A test file
{id: writing-unit-tests}
![](examples/modules/app/t/01-load.t)


## Writing Tests
{id: writing-tests}

```
ok($condition, $name);

is($actual, $expected, $name);

like($actual, qr/$expected/, $name);

use_ok('Module::Name');

TODO: {
   local $TODO = "Some excuse";
   is(add(1,1,1), 3, "adding 3 numbers");
}

diag "Some message";

diag explain @data_structure;
```

```
Test::Most
Test::NoWarnings  or Test::FailWarnings
Test::Exception  or the newer  Test::Fatal
Test::Warn
Test::Deep

Devel::Cover
```



## Exercises: Multiply numbers
{id: exercise-multiply-numbers2}

* Write a script with a function to multiply numbers **sub multiply**.
* Once it is ready move the multiply subroutine to the library.pl file that already has the **add** subroutine and write a script that can use it.
* Create a package called Exercise::Calc that will export the multiply function.  Write a script that will use this module and the given functions.
* Write a few test cases for both the add and multiply functions. Including test cases where you try to add 3 or more numbers. As the tests are failing, mark them as TODO.
* Fix the add() function so it passes its new tests with 3 or more parameters.
* Add short user documentation that can be read by perldoc.
* Create the files necessary for distributions and make sure you can generate the tar.gz file.



## Solution: Multiply numbers
{id: solution-multiply-numbers2}
![](examples/modules/library_multiply.pl)


## Overview
{id: perl-modules-overview}

* Code reuse
* Perl4 style was putting functions in library files and "require"-ing the files
* Danger of redefining other functions
* Perl Modules are namespaces
* Main name space is called main, separation is done using :: so variable $x in the main script are actually called $main::x
* Within a namespace you can use any function
* This does not redefine any function in the other namespaces

[How to create a Perl Module for code reuse?](https://perlmaven.com/how-to-create-a-perl-module-for-code-reuse)

