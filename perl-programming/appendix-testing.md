# Appendixes
{id: appendix-testing}

## Test related CPAN Modules
{id: test-related-cpan-modules}


<a href="http://metacpan.org/pod/Task::Test">Task::Test</a>
A collection of testing related modules with some explanation
on each one of them.



* Test  - this is obsolete
* Test::Tutorial
* Test::Simple
* Test::More
* Test::Harness
* Test::DatabaseRow



## Generic modules
{id: generic-cpan-modules}

* File::Find
* File::Find::Rule



## Web testing
{id: cpan-modules-for-web-testing}

* Test::HTML::Lint
* HTML::Lint
* LWP
* LWP::Simple
* WWW::Mechanize
* HTTP::Recorder
* HTTP::Proxy



## GUI testing
{id: cpan-modules-for-gui-testing}

* Win32::GuiTest
* Win32::GUIRobot
* X11::GUITest



## Other sources of information
{id: other-sources-of-information}

* Slides about [automated testing by Andy Lester](http://www.petdance.com/perl/automated-testing/).
* An [overview of the test modules](http://qa.perl.org/test-modules.html).
* Perl [Quality Assurance](http://qa.perl.org/) Projects.
* [Whirlwind Tour of Test::Class](http://www.slideshare.net/Ovid/a-whirlwind-tour-of-testclass) by Ovid.
* Testing presentation via the [Perl TV](http://perltv.org/tag/testing).
* [Open Source Testing tools](http://www.opensourcetesting.org/).
* [Perl Test Refcard](http://langworth.com/pub/perl_test_refcard.pdf) by Ian Langworth.



## Test Realistically
{id: test-realistically}

* Use the application according to its documentation.
* Use it according to common sense.



## Test Unrealistically
{id: test-unrealistically}

* Test for edge cases:
* - negative values, 0, 1, -1, very big numbers.
* - characters instead of numbers, floating point instead of whole numbers.
* - empty string, very long string, strange characters.
* Test randomly.
* Test using invalid input.



## File System testing
{id: manual-filesystem-testing}


When testing a file system one wants to make sure that
the system operates reliably under various conditions. In no case will
it loose data, not even in extreme cases such as many small files or few
large files that could fill an entire disk.




Applications should be prepared for testing. For example in a Windows GUI application every
control should have a unique and persistent name so we can use that name to find the handle.
Testing the fact that every is control has a name is already one element in our testing suit.






