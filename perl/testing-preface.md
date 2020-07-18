# Preface
{id: testing-preface}

## Why Test?
{id: why-test}

* Do you deserve to be confident?
* Can you sleep at night?
* Testing is Fun!



## What are automated test?
{id: what-are-automated-test}


Just some more code that uses your functions/modules/application/etc.




## Manual testing
{id: testing-manual}

{aside}

Before we dig into the world of automated testing we should see that we are
speaking about the same thing.
{/aside}

1. Who tests their application manually?
1. What kind of application?



## Why Automate?
{id: why-need-automation}

1. Why do we need automated tests when we can test manually?
1. Isn't that just waste of time/money?
1. We could add more features instead.


{aside}

Mostly for the regression but in some cases it is very hard or
impossible to test manually.

Writing tests can be a huge expense.
Running tests the 2nd time is where you start to see the benefit.
After 10 or 100 times you'll really see the profit.
{/aside}


## Functional Testing
{id: functional-testing}

What kind of tests are we going to talk about here?



Not scalability, nor performance, nor security, ...



{aside}

In this course, we are mostly going to talk about functional testing though one can handle security the same way.
{/aside}


## Unit/Integration/Acceptance Test
{id: unit-testing}


What's the difference between them?



{aside}

Mostly just the scope and who writes them.
{/aside}

{aside}

The advantage of unit tests, that is code checking small parts of the application
is the ability to focus on a small part of the code. It's easier to test
and it's easier to understand/debug etc.
{/aside}

{aside}

Separation of concerns in small units. Every module should do only one thing.
{/aside}

{aside}

E.g. if you are building a log analyzer that analyzes Apache
log files and spits out HTML reports.
Most of us would just write some code to read in the file line by line,
process each line and at the end create the HTML report. All in one script.
{/aside}

{aside}

A probably better approach is to create a module for reading the file.
A separate module to parse the line and build some data structure from the
data. Then a third module that generates accumulated data and a 4th module
to create the HTML report. This will allow testing the individual components
separately and it will allow the reuse of those components. For example
when you want to create a PDF version of the same report you just need
to replace the final module in the chain.
{/aside}


## White box and Black box testing
{id: white-box-testing-black-box-testing}

* Black box testing is when we only use the external interface (e.g. GUI) of the application.
* White box testing is when we also check the internals. E.g. access the database directly.



## Objectives of the course
{id: objectives-of-the-course}

* Why and when to test ?
* Learn about the tools Perl provides for automated testing.
* Use the test framework provided by Perl.



## Plan of the seminar
{id: plan-of-the-seminar}

Part 1 - Perl Testing framework


1. Introduce the Perl modules for basic testing framework.
1. Testing Perl function and modules.
1. TAP - the Test Anything Protocol


Part 2 - Test Anything else using Perl


1. Command line applications, devices with CLI access.
1. Browser based web applications
1. Databases.
1. X Windows.
1. Microsoft Windows GUI Applications.



## Process of testing
{id: process-of-testing}

1. Create fixture (set up environment).
1. Run test.
1. Analyze results.
1. Tear down (clean up environment).







