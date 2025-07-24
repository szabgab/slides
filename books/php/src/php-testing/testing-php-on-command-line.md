# Testing PHP on the command line

Running the test using the web browser will work well during the development
of each test and the relevant code but as the number of tests grow we
will prefer to automate this process and execute it by some automated tool.
Eg. crontab on unix, the scheduler on windows, a smoke testing system
or the post commit hook of your version control system. That will only work if
we can run our tests from the command line.


Luckily SimpleTest and the autorun.php can let us do this.
We can take the last example and run it from the command line:


```
$ php examples/php/simpletest/st04.php
```

The Output is quite similar to what we have in the browser but
this is without any colors.


{% embed include file="src/examples/php/simpletest/st04.out)


We can now create a batch file and run all the test files we might have from the
command line. We'll come back to this later.








