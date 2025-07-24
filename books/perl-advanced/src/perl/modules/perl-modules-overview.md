# Overview


* Code reuse
* Perl4 style was putting functions in library files and "require"-ing the files
* Danger of redefining other functions
* Perl Modules are namespaces
* Main name space is called main, separation is done using :: so variable $x in the main script are actually called $main::x
* Within a namespace you can use any function
* This does not redefine any function in the other namespaces

[How to create a Perl Module for code reuse?](https://perlmaven.com/how-to-create-a-perl-module-for-code-reuse)



