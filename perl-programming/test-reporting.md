# Running and reporting tests
{id: test-reporting}

## TAP - Test Anything Protocol
{id: tap}
{i: TAP}
{i: IETF}

```
1..3
ok 1
ok 2
not ok 3 
```

{aside}

All printing of "ok" and "not ok" are part of TAP - Test Anything Protocol.
{/aside}

{aside}

Work is under way to turn it into an IETF standard.

We run our test scripts either using plain perl, or via prove or make test.
They all generated textual output. Some very verbose, others a more concise
aggregate report of the results. None of them is really pleasing to the eye.
{/aside}


## prove
{id: prove-options}
{i: prove}

```
prove

prove -h          Help
perldoc prove

prove -r          Recursive
prove -v          Verbose
prove -l          -Ilib
prove -b          -Iblib/lib -Iblib/arch


prove -s          shuffle (random order)

prove --timer     Show elapsed time for each script

prove --exec '/usr/bin/ruby -w' t/
```


## Parallel testing
{id: parallel-testing}

```
prove -j4         Run test scripts in parallel
~/.proverc        Can have values like -j4 in it
                  then use -j1 to run sequential
```

* Shared resources? (database, temp files, sockets, etc.)
* Are the test script independent? (setup fixture, teardown in every file.)




## prove --state
{id: prove-state}

* prove --state=save          will save the status of the meta data of the test run in .prove
* prove --state=failed        will run the test scripts that failed last time (based on .prove)
* prove --state=failed,save   run the failed tests and update .prove
* prove --shuffle --state=save  Run in random order and save it in .prove
* prove --state=last            Run the same order as last time (the result of shuffle)
* prove --state=todo            Run the test scripts with TODO entries
* prove --state=slow -j4        Run the slowest test first (but then 4 in parallel)



## Parse TAP from a file
{id: prove-parse-tap-from-a-file}

{aside}

Prove tricks from Michael G Schwern on the perl-qa list.
{/aside}

{aside}

Parse TAP from a file, rather than program output.  Handy for doing
experiments without having to mock up a program.
{/aside}
![](examples/foo.tap)

**prove --exec 'cat' examples/foo.tap**


```
examples/foo.tap .. ok
All tests successful.
Files=1, Tests=2,  0 wallclock secs ( 0.04 usr +  0.01 sys =  0.05 CPU)
Result: PASS
```


## prove - run other executables
{id: prove-run-other-executables}

{aside}

Make prove run tests as executables with no interpreter.  Useful for mixed
language environments and tests written in compiled C.  Just make sure your
tests have the executable bit set and that you're using an unambiguous path to
the test (ie. not "test.t" but "./test.t") so prove doesn't search your $PATH.
{/aside}


```
$ ls -l
total 12K
-rwxrwxr-x 1 schwern schwern 53 2009-02-25 17:30 test.perl
-rwxrwxr-x 1 schwern schwern 53 2009-02-25 17:31 test.ruby
-rwxrwxr-x 1 schwern schwern 42 2009-02-25 17:31 test.sh

$ prove --exec '' t/test.*
t/test.perl....ok
t/test.ruby....ok
t/test.sh......ok
All tests successful.
Files=3, Tests=6,  0 wallclock secs
   ( 0.04 usr  0.02 sys +  0.00 cusr  0.01 csys =  0.07 CPU)
Result: PASS
```


## TAP::Formatter::HTML by Steve Purkis
{id: tap-html}
{i: TAP::Formatter::HTML}
{i: HTML}
{i: prove}


The simplest way to generate nice reports is to use [TAP::Formatter::HTML](https://metacpan.org/pod/TAP::Formatter::HTML).
Instead of running prove alone, you can pass it a class implementing formattion
options and it will use that instead of the default textual output.

<command>prove -b -m -Q --formatter=TAP::Formatter::HTML examples/tap > output.html</command>

[output]("../test-automation-using-perl/examples/tap/HTML/output.html)


## Collection Test reports
{id: collecting-test-reports}


Collect the report with <command>prove -b -a tap.tar.gz  examples/tap</command> and save it on a centralized server.



{aside}

You don't always want to install the TAP::Formatter::HTML on
every system you run your tests. After all you might not even
use Perl for generating the TAP stream so we should have a way to
collect the results of the TAP streams. Move them to a central
machine and generate the nice reports there.


This will run the tests and generate a tarbal from the resulting
TAP stream along with a meta.yml file that contains some meta data
on the execution. You can take this file and move it to another
server. (A warning though, the TAP streams of each test file is saved in
a file with the exact same name as the test file was. So if you create the
archive and the untar it you will overwrite your test scripts with the
TAP streams. Better to open it in another directory.
{/aside}


## Generating HTML reports from Archives
{id: generating-html-reports-from-archives}

{aside}

Once you have the tar.gz file on the central machine you should
be able to create the HTML report.
Unfortunately I could not find a nice way to do it but with the help
of Ash Berlin and Steve Purkis we came up with workaround:

First unzip the file using

    tar xzf tap.tar.gz

Then you can run the following command:

    prove --exec 'cat' -Q --formatter=TAP::Formatter::HTML t/ > output.html

This will only work on Unix, maybe on Windows one can replace 'cat' with
'type' but I have not tried it. In any case I hope soon there will a better
solution to this.
{/aside}



First unzip the file using <command>tar xzf tap.tar.gz</command>




Then you can run the following command




<command>prove --exec 'cat' -Q --formatter=TAP::Formatter::HTML t/ > output.html</command>




## Smolder
{id: smolder}
{i: Smolder}

{aside}

Smolder is a web based application to collect and display TAP streams.
It is already available on CPAN. Once installed it can be launched with the smolder
command. By default it provides its own web server and uses SQLite so you don't have
to worry about further configuration. Once you see it and decide that you'd like to use
it in production with many test systems reporting to it then you'll probably invest more
in the installation, use Apache as the front-end server and MySQL as the database but
at the beginning you can use the simple installation.

Once the system is setup you have a web based administrative interface to add projects,
users and associate them with each other. Every user can then upload archived
tap results as generated by the -a flag of prove. The system then provides various views
of the tests results. You can view the details of a single test run and you can already
see some historical data as well.
As of version 1.35 you have to do the following to start the server:

create ~/.smolder and in it create ~/.smolder/smolder.conf with one line:

HostName    smolder.local

In addition you have to change the /etc/hosts file so smolder.local will resolve
to 127.0.0.1 (You can of course use any name with at least one . in it.)

Then you can launch Smolder using the following command:

smolder -c ~/.smolder/smolder.conf

Then you can use your browser to access  it.

The password for the "admin" user is "qa_rocks".
{/aside}


[Smolder](https://metacpan.org/pod/Smolder) by Michael Peters.

`smolder_smoke_signal --server smolder.foo.com:port --username myself --password s3cr3t --file tap.tar.gz --project MyProject`


## Exercise: Smolder
{id: exercise-smolder}


Check if Smolder is already installed and start it.
Add one or more users to it and at least one project and create some associations.
Then run the prove command with the archiving option on the examples/tap files and upload
the resulting file manually using your browser.




Change the test scripts a bit adding more tests. Change tests from success to failure and
from failure to success. After every change run the tests again generating the archive file
and upload it to Smolder. The first few results you should upload manually but later switch
to the use of Smolder smoke signaler.






