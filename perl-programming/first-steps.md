# First steps
{id: first-steps}

## Installation
{id: installation}

* On UNIX/Linux you usually have it installed in **/usr/bin/perl**
* On Microsoft Windows install ActivePerl from [ActiveState](http://www.activestate.com/)
* Better yet, download [Strawberry Perl](http://www.strawberryperl.com/)
* [DWIM Perl for Windows](http://dwimperl.com/) (and Linux) - not maintained any more.
* [Citrus Perl](http://www.citrusperl.com/)
* [Installing and getting started with Perl](https://perlmaven.com/installing-perl-and-getting-started)
* [Download and install Perl](https://perlmaven.com/download-and-install-perl)



## Editors
{id: perl-editors-ide}

* [Emacs](http://www.gnu.org/software/emacs/)
* [vi, vim, gvim ](http://www.vim.org/)
* [Kate](http://kate-editor.org/)
* [Gedit](http://projects.gnome.org/gedit/)
* [Atom](https://atom.io/)


* [Notepad++](http://notepad-plus-plus.org/)
* [Textpad](http://www.textpad.com/)
* [Ultra Edit](http://www.ultraedit.com/)


* [TextMate](http://macromates.com/)



## IDEs
{id: perl-ide}

* [Komodo of ActiveState](http://www.activestate.com/)
* [Eclipse](http://www.eclipse.org/) with EPIC or Perlipse
* [Jetbrains IntelliJ IDEA](https://www.jetbrains.com/idea/) + perl plugin.
* [Padre, the Perl IDE](http://padre.perlide.org/) (bundled with [DWIM Perl](http://dwimperl.com/)) (not maintained any more)
* [Perl Editor](https://perlmaven.com/perl-editor)



## Perl on the command line
{id: perl-on-the-command-line}
{i: -e|options}
{i: -v|options}


On the command line one can type:



* **perl -e "print 42"**
* **perl -v**
* **perl -V**
* **perl -E "say 42"**




See Perl One-liners.




## First script
{id: first-script}
{i: string}
{i: number}
{i: "}
{i: ;}
{i: print}
{i: \n}
{i: sh-bang}

![](examples/intro/hello_world.pl)


run it by typing
`perl hello_world.pl`

On unix you can also make it executable:
`chmod u+x hello_world.pl`
and then run like:
`./hello_world.pl`

A couple of notes

* Strings and numbers
* Strings must be quoted, you can use special characters such as "\n"
* The **print** statement (Output) - gets comma delimitered list of things
* ; after every statement



## Safety net
{id: safety-net-strict-warnings}
{i: -w|options}
{i: strict}
{i: warnings}
{i: diagnostics}

```
#!/usr/bin/perl
use strict;
use warnings;
```

You should always use them as they are a safety net helping reduce mistakes.


It is usually very hard to add this safety net after you already have some code.


If the warnings you get don't make sense add


```
use diagnostics;
```

line and you will get more verbose warnings.




Why are use warnings and use strict so important even in small (&lt; 100 lines) scripts ?



* Help avoiding trouble with recursive functions
* Help avoiding typos in variable names
* Disable unintentional symbolic references
* Reduce debugging time
* Enable/enforce better coding standard => cleaner code, maintainability


* [Always use strict and use warnings in your perl code!](https://perlmaven.com/always-use-strict-and-use-warnings)
* [Always use warnings in your Perl code!](https://perlmaven.com/always-use-warnings)



## First sub
{id: first-script-with-main}
{i: sub}

![](examples/intro/hello_world_main.pl)


* Putting all your code in small(!) functions will make your code better.



## First say
{id: first-script-with-say}
{i: say}

![](examples/intro/hello_world_say.pl)


## print vs. say
{id: print-vs-say}

```
say  "hello";    # print a newline at the end. (available since perl 5.10)
print "hello";   # print as it is
print "hello\n"; # print a newline at the end.
```


## Debugging
{id: debugging}
{i: -d|options}
{i: debug}
{i: Devel::ptkdb}

* Running script **perl mycode.pl**
* Use the built-in debugger **perl -d mycode.pl**
* Install Devel::ptkdb and run ** perl -d:ptkdb mycode.pl**
* IDEs have debuggers
* Include print statements in the critical places of your code.
* **use Data::Dumper qw(Dumper);**



## Avoid global variables
{id: avoid-global-variables}


* Not really Perl specific, but declare variables as late as possible!
* Don't use global variables!
* You will thank yourself a year later.



## Keep it Simple - KISS
{id: keep-it-simple}


* A script has to be simple, readable and reusable.
* Sophisticated optimization and algorithms are less interesting.




## Comments
{id: comments}
{i: #}

```
# Comments for other developers

print 42; # the answer
```


## Perl documentation
{id: perl-documentation}
{i: perldoc}

* `perldoc perl`
* `perldoc perlsyn`
* `perldoc perlfunc`
* `perldoc -f print`
* `perldoc -q sort`
* `perldoc perlrun`
* `perldoc strict`
* `perldoc warnings`

Web based: [perldoc](http://perldoc.perl.org/)

[Core Perl documentation and CPAN module documentation](https://perlmaven.com/core-perl-documentation-cpan-module-documentation)


## POD - Plain Old Documentation
{id: pod-plain-old-documentation}
{i: POD}
{i: =head1}
{i: =head2}

![](examples/intro/documentation.pl)

* `perl examples/intro/documentation.pl`
* `perldoc examples/intro/documentation.pl`

[POD - Plain Old Documentation](https://perlmaven.com/pod-plain-old-documentation-of-perl)


## Exercise: Hello world
{id: exercise-hello-world}

Try your environment:

* Make sure you have access to the right version of Perl (5.8.x) or newer
* Check you can read the documentation. (perldoc)
* Check if you have a good editor with syntax highlighting
* Write a simple script that prints     Hello world
* Add comments to your code
* Add user documentation to your code

