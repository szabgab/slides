# Makefile.PL for ExtUtils::MakeMaker

Makefile.PL
ExtUtils::MakeMaker

{% embed include file="src/examples/distribution/project_with_extutils_makemaker/Makefile.PL" %}


In this example Makefile.PL we have to say what is the name of the
module, and in which file is the version number - this value will be
part of the generated filename. The LICENSE field is a relatively
new addition. In this example I am using the "perl" license
but if you are writing this for a company then you'll probably
use the word "restrictive".

Once you have setup the directory structure and created a simple
Makefile.PL you can type the following:


```
$ perl Makefile.PL
$ make
$ make test
```


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


```
$ make manifest
$ make dist
```



