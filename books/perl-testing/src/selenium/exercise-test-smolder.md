# Exercise: Testing Smolder

In an earlier chapter we used Smolder to collect results of the test executions.
Smolder itself is a web application using Javascript. Let's test it.

Let's start by assuming smolder is running and try to access its front page and login with
an existing user.

Then we should try to create a new user and log in with that.

After that, as we cannot really know which user is still available let's
create a new .smolder directory in some temporary place (use File::Temp for this).
Create a configuration file, launch Smolder and then access it using your test script.



