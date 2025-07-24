# Why use Docker?



One of the big problems in software development is the fact that the environment where we develop our code is different from
the environment where QA will test the code that is different from the environment where the application will run in production.



This difference can be as simple as having different operating systems, e.g. a developer might use Windows, Linux, or Mac on her desktop
while the production runs on a Linux box. Even if they would use the same operating system, certain dependencies and libraries
installed on these machines might be different. There are various ways to reduce the risk that arises from these differences, one of the
latest and best is the use of some kind of virtualization.



Docker is the most popular system to provide virtualization.


* One of the big problems: Developers, Testers, and Production all have different environments.
* Dependency hell.
* On-boarding new developers is hard.

* Makes it easy to have the exact same setup for development, testing, productions.
* Makes it easy for people to set up their development environment.


