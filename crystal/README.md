REPL
gets without nil
compile with optimization flags --release
pointers? is this only for bindings or have other uses?


* Implement the exercises in the Python course
* Create a web application

* Write a test for https://github.com/watzon/octokit.cr that will use a secret stored in GitHub Actions to use the API

* Modules
* Classes

* Read shard.yml file in particular
* Web application development?
* Access to SQLite?
* Access to MongoDB?



## Ideas for slides


I run
crystal example.cr
I get
Showing last frame. Use --error-trace for full trace.
crystal --error-trace example.cr
I get Error: unknown command: --error-trace
I need to run
crystal build --error-trace example.cr
to get the nice stack trace

filter or grep => reject   (use the names other languages use for the same concept to make it easier to find the right words )

What is "flag?"  ? I saw it in the source code of Kemal, but I don't see it defined anywhere.


Yak Shaving

https://forum.crystal-lang.org/ has around 500 users.
https://gitter.im/crystal-lang/crystal Gitter 1960 people

Crystal Learning Resources
LuckyCast https://luckycasts.com/   ( https://luckyframework.org/ )

Rosetta Code: http://www.rosettacode.org/wiki/Category:Crystal
Crystal:  255 pages
Ruby:   1,020 pages
Perl:   1,296 pages
Python: 1,242 pages
Go:     1,372 pages

Exercism https://exercism.io/
  Crystal: 50 Exercises   3 Mentors   1,171 Students
  Ruby:    98 Exercises 116 Mentors  31,976 Students
  Perl:    62 Exercises   7 Mentors   1,655 Students
  Python: 117 Exercises 157 Mentors 123,833 Students
  Go:     109 Exercises  72 Mentors  48,035 Students

LinkedIn pages:
 https://www.linkedin.com/company/crystal-language/ 56 followers
LinkedIn groups:
 The Crystal Programming Language https://www.linkedin.com/groups/12419254/  6 members
 Crystal Language https://www.linkedin.com/groups/12061584/ 36 members

Facebook
Twitter
Instagarm
Reddit
Stack Overflow
What else?

What learning resoureces are there?

Crystal Course of Bruce A. Tate https://grox.io/language/crystal/course Nov 1, 2019


### SQLite

Lack of documentation
last_id  last_insert_id  How can one know?

puts __FILE__

* Compiles to LLVM

* Macros for meta-programming
* Concurrency via CSP
* Bind to C libraries
* Standard library

* Doc generation
* Test framework
* Common Code formatting
* Dependency management

Ruby to Crystal
* Replace string with single-quotes by strings with double-quotes or %{}
* Source is in the src/ directory and not in the /lib directory

local/global variables and constants.
