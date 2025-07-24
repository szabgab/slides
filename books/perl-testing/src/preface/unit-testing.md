# Unit/Integration/Acceptance Test


What's the difference between them?

Mostly just the scope and who writes them.

The advantage of unit tests, that is code checking small parts of the application
is the ability to focus on a small part of the code. It's easier to test
and it's easier to understand/debug etc.

Separation of concerns in small units. Every module should do only one thing.

E.g. if you are building a log analyzer that analyzes Apache
log files and spits out HTML reports.
Most of us would just write some code to read in the file line by line,
process each line and at the end create the HTML report. All in one script.

A probably better approach is to create a module for reading the file.
A separate module to parse the line and build some data structure from the
data. Then a third module that generates accumulated data and a 4th module
to create the HTML report. This will allow testing the individual components
separately and it will allow the reuse of those components. For example
when you want to create a PDF version of the same report you just need
to replace the final module in the chain.



