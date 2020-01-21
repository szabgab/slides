# Real world?
{id: real-world-applications}

## Why test?
{id: why-test}

* Business Value



## How to test?
{id: how-to-test}

* Manual - exploratory
* Automated - regression




## Manual Tests (exploratory tests)
{id: manual-tests}

* New feature is working
* Bug was eliminated
* General view of the system



## Automated Tests (regression tests)
{id: automated-tests}

* Avoid regression
* Better Software Design (TDD)
* Your Sanity



## Two cases of Automated tests
{id: tdd-vs-real-world}

* TDD
* Real world



## Real World
{id: real-world-testing}

* Application mostly works
* Huge system
* Interdependent code
* Long functions
* It is hard to test parts of the system



## Testing modes
{id: testing-levels}

* Unit testing
* Integration testing
* Acceptance testing (BDD ?)




## Testing Environment
{id: testing-environment}

* Git
* Virtualization (Docker? VirtualBox?)
* One-click and fast setup



## Setup - Fixture
{id: setup-fixture}

* Web server
* Databases
* Windows machines
* Other devices
* External services




## Fake the world
{id: fake-the-world}

* Simulator
* Mocking
* [Monkey patching](https://en.wikipedia.org/wiki/Monkey_patch) = runtime changing of code.




## Test Double
{id: test-doubles}

* [Martin Fowler](https://martinfowler.com/): [Mocks aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html)
* [Gerard Meszaros](http://xunitpatterns.com/gerardmeszaros.html): [XUnit Patterns](http://xunitpatterns.com/)


Test Doubles


* Dummy
* Fake
* Stubs
* Spies
* Mocks





## Mocking what?
{id: mocking-what}

* User created functions (or classes)
* 3rd party functions (or classes)
* Functions that are part of the language
* System calls (STDIO, files, time, etc.)
* Whole fiilesystem
* Database
* Network access
* External device/service



## Fake (temporary) filesytem
{id: temporary-filesystem}


Use temporary directories and files - locate pathes that are hard-coded in the code and replace them with configuration options from a configuration file or environment variables.
<a href="https://metacpan.org/pod/File::Temp">File::Temp</a>



```
use File::Temp qw(tempdir);
my $dir = tempdir( CLEANUP => 1 );
```


## Fake library
{id: fake-library}


Have a private implementation of the used library and make sure this one gets loaded instead of the real class. (e.g. by tweaking @INC and loading the module early.


![](examples/fake-module/t/lib/WWW/Mechanize.pm)


## Use the real library
{id: use-the-real-library}
![](examples/fake-module/t/use_real.t)


## Use the fake library
{id: use-the-fake-library}
![](examples/fake-module/t/use_fake.t)


## Mocking IO - module
{id: mocking-io-the-module}
![](examples/mocking_io/MyModule1.pm)


## Mocking IO - test
{id: mocking-io-test}
![](examples/mocking_io/test1.t)


## Mocking IO
{id: mocking-io-module2}
![](examples/mocking_io/MyModule2.pm)


## Mocking IO - test
{id: mocking-io-test2}
![](examples/mocking_io/test2.t)


## Mocking IO - script
{id: mocking-io-script}
![](examples/mocking_io/game.pl)


## Mocking IO - test script
{id: mocking-io-test-script}
![](examples/mocking_io/test_game.t)


## Mocking function of web access
{id: mocking-function-of-web-access}

* [Test::Mock::Simple](https://metacpan.org/pod/Test::Mock::Simple)
* [Mocking function to fake environment](https://perlmaven.com/mocking-function-to-fake-environment)

![](examples/mocking-functions/MyWebAPI.pm)


## Test live web server
{id: test-live-web-server}
![](examples/mocking-functions/webapi.t)

```
1..1
not ok 1
#   Failed test at webapi.t line 14.
#     Structures begin differing at:
#          $got->{Miley Cyrus} = '4'
#     $expected->{Miley Cyrus} = '3'
# Looks like you failed 1 test of 1.
```


## Mocking the get method
{id: mocking-the-get-method}
![](examples/mocking-functions/fake_webapi.t)

```
1..1
ok 1
```


## More test cases
{id: more-test-cases}
![](examples/mocking-functions/more_webapi.t)


## Test exception
{id: test-for-exceptions}
![](examples/mocking-functions/exception_snippet.t)

```
1..2
ok 1
Something went wrong at exception.t line 25.
# Looks like you planned 2 tests but ran 1.
# Looks like your test exited with 255 just after 1.
```


## Linewrap bug
{id: linewrap-bug}
![](examples/mocking-functions/linewrap_snippet.t)

```
1..4
ok 1
ok 2
ok 3
not ok 4
#   Failed test at linewrap.t line 46.
#     Structures begin differing at:
#          $got->{Miley Cyrus} = '1'
#     $expected->{Miley Cyrus} = '2'
# Looks like you failed 1 test of 4.
```


## Mocking time: the session module
{id: mocking-time-the-session-module}

* [Test::MockTime](https://metacpan.org/pod/Test::MockTime)
* [Testing sessions by mocking time](https://perlmaven.com/testing-session-mocking-time)

![](examples/mock-time/MySession.pm)


## Test session timeout
{id: test-session-timeout}

Takes 61 seconds to run...

![](examples/mock-time/time.t)


## Test session timeout faking the time
{id: test-session-timeout-faking-the-time}
![](examples/mock-time/fake_time.t)



## Testing a database driven application
{id: testing-database-driven-applications}

* Have a set of test data (small set of data)
* Have a copy of the production data
* Use an in-memory database for testing to make it much faster than a disk-based one.
* Mock the database access
* [DBD::Mock](https://metacpan.org/pod/DBD::Mock)
* [DBI::Mock](https://metacpan.org/pod/DBI::Mock)



## Build Schema by code
{id: build-schema-by-code}


Have scripts that can create the database schema and load the initial data and scripts for migration among schema versions.




## Manual Schema change
{id: manual-schema-change}


Have DBAs (or developers) change the schema manually on the development and later on the production server. As a minimum have some
code that will regularly dump the schema and add it to some version control system.




## Mocking in Java
{id: mocking-in-java}

* [EasyMock](http://easymock.org/)
* [JMock](http://www.jmock.org/)
* [Mockito](http://site.mockito.org/)
* [JMockit](http://jmockit.org/)




## How to move forward?
{id: how-to-move-forward}

* Hard to justify as it usually does not find (new) bugs.
* Write tests for new features
* Write tests for bugs reported



## How to find bugs?
{id: how-to-find-bugs}

* Use a linter.
* Turn on stricter compilation (and runtime) warnings.



## How to find bugs in Perl?
{id: how-to-find-bugs-in-perl-code}

```
use strict;
use warnings;
```

Run Perl::Critic on the code.




## Testing culture
{id: testing-culture}

* Automated tests are like insurance.
* Get management support
* Build a culture





