# Perl slides


## Dancer

Reload when config changes
plackup -R lib,environments bin/app.psgi

  how to run plackup in debug mode to see the detailed error message?

route with regex?
route variable that can accept slashes as well

redirection

url_for ?
showing static
files

same function for both GET and POST
separate functions for GET and POST

Deploy Dancer application to the cloud
Dancer in Docker

Exercise: Random redirect

Create our own 404 page and 500 page
Show elapsed time on every page

JSON API
Some JavaScript client

Session?

dancer -a
Templates
   single value
   if
   if else
   loop
   hash
   commafy
   - exclude newlines
   array of hashes
   include other templates
   extend template

DBI
Bootstrap
Oracle XE + Data Tables  https://datatables.net/


Dancer app metacpan front end
Make it easy to run it locally in dockerAllow the user to save the data file locally (single user mode/ multi user mode?) Select modules and display their documentation

/author/szabgabShow list of packages, which one is lacking vcs, which one is lacking bug tracking system, Which one has rtHow many open bugs do each one have? 
A stats page similar to cpan. Rocks, but maybe add paging. 


## Functional programming

https://metacpan.org/pod/List::Util    functions (e.g. first, all, none)

Dispatch table

Callback functions

Memoization

Manipulating functions by functions (add logging before and after the function call)


## Testing

- Test::Class
- How to set up fixtures?

BDD https://metacpan.org/release/Test-BDD-Cucumber


## OOP


## Other

AUTOLOAD -> https://perlhacks.com/articles/symbolapproxsub/

## Algorithms

Linear search
Binary search
Linked Lists
Binary tree
Tree
Hashing


## Parallel processing, forking

Add a page linking to the slides and linking to the GitHub page to download the source code.

Show an example where forking makes the process slower.

Parallel::Forkmanager - can it reuse the same child processes for multiple tasks?
What if we have many task and fewer processes?
Show PFM with some sleeping in the child process and show that if we have
many tasks it still only runs N in parallel.
Show when is the run_on_finish called, immediately after on finishes (and before the replacement is executed)
or only at the end.
Create a queue to be processed.

## Threading

https://metacpan.org/pod/Thread::Queue

## Async

https://www.reddit.com/r/perl/comments/l5blnf/async_programming/

AnyEvent, IO::Async
Future::AsyncAwait
POE
Mojo
Mojo::IOLoop  https://docs.mojolicious.org/Mojo/IOLoop
https://docs.mojolicious.org/Mojolicious/Guides/Cookbook#CONCEPTS



## Topics

The global scalar special variables.

About large-scale software development in Perl. I understand Perl syntax and scripting very well, but how do I apply that to a large organization using perl?
Example topics: automated testing, code review, linting, refactoring, application monitoring, proper code layout, dependency management/injection, and the proper usage of large objects.

How to deal with extremly large CSV file - read line-by-line.
Parse::CSV

Example using continue: https://metacpan.org/pod/perlfunc#continue-BLOCK
Example using given https://perldoc.perl.org/perlsyn#Switch-Statements


OpenCV with Perl

## References in Perl

* references to function (lookup table, passing function as a parameter)
* no need to pass scalar as a parameter to Getopt::Long
* Use scalar ref to open a string as if it was STDIN or STDOUT (or a file)

