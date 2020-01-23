# Command line application
{id: command-line}

## bc - An arbitrary precision calculator language
{id: bc}

It is much more than a calculator, it is a language.
Luckily we don't need to learn the whole language in order to
to do simple calculations.
Normally you execute 'bc' from the command line and then you type in
your calculations. Pressing ENTER will do the calculation.




## Normal operation
{id: bc-normal-operation}

```
<command>$ bc</command>
bc 1.06
Copyright 1991-1994, 1997, 1998, 2000 Free Software Foundation, Inc.
This is free software with ABSOLUTELY NO WARRANTY.
For details type `warranty'.
<command>23+7</command>
30
<command>quit</command>
$
```

Try it ....



## Expect.pm
{id: expect}
{i: expect}


[Expect.pm](https://metacpan.org/pod/Expect) written by Austin Schutz and maintained by Roland Giersig



* Provides a way to describe user behavior in a command line environment.
* Can send information as if it was typed on the keyboard.
* Can wait for some Expect-ed value and based on this value do something.
* Originally an extension of Tcl.
* Ported to Perl.
* Can be used in environments such as:
* Works on Linux/Unix/OSX.
* Does NOT work on MS Windows.


* Command line application like bc.
* Telnet to another box and type in things.
* Anything usually a person would do on the command line.




## Simple computation - adding two values
{id: expect-simple-computation}
![](examples/bc/bc1.pl)

* raw_pty turns off echo
* spawn starts the external program
* expect(timeout, regex) return undef if failed
* timeout is in seconds, 0 means check once, undef means wait forever
* send - as if the user was typing at the keyboard


```
```


## Results
{id: expect-simple-computation-result}

```
<command>$ perl examples/bc/bc1.pl</command>
```
![](examples/bc/bc1.pl.out)


## Reduce output - turn it into a test script
{id: expect-reduce-output}

We don't want to see all the output bc generates and then try to look
for the correct responses or the error messages. We'd prefer just see ok or not ok

![](examples/bc/bc4.pl)

* $e->log_stdout(0); - turn off the printing to the screen



## Output
{id: expect-reduced-output}

```
<command>$ perl examples/bc/bc4.pl</command>
```
![](examples/bc/bc4.pl.out)


## Expect and BAIL_OUT
{id: expect-bail-out}

```
<command>$ perl examples/bc/bc41.pl</command>
```
![](examples/bc/bc41.pl)



## More than one test
{id: expect-more-than-one-test}

We can then setup lot's of tests and run them through one invocation of bc.

![](examples/bc/bc5.pl)



## Output
{id: expect-more-than-one-test-output}

```
<command>$ perl examples/bc/bc5.pl</command>
```
![](examples/bc/bc5.pl.out)


## External test file
{id: expect-external-test-file}

Separating the test cases from the code.

![](examples/bc/bc5a.pl)
![](examples/bc/bc5a.pl.out)


## Random regression tests
{id: expect-random-regression-test}


The idea is that we don't have time to manually setup hundreds of tests and calculate our expectations
so instead we compare some random tests to the results of a previous run.




We can log the results of each operation in a file and compare
the resulting files to some previous execution.



* Create a set of random operations
* Because we don't have time to check all the results we only check if there were no error messages, but in general we don't care about the correctness of the results
* Record the tests and the results
* Run the tests again with the a version (now they are not random any more) and check if any of the results has changed. If something changed it indicates that either earlier or now we have a problem
* Investigate the differences and include the problematic tests in the manual test suit
* Either save the new results as the new expectation or discard it and discard the current version of the application



## Random and regression testing
{id: expect-random-and-regression-test}
![](examples/bc/bc6.pl)


## Random and regression testing - slight improvement
{id: expect-random-and-regression-test-diff}
![](examples/bc/bc7_diff.pl)


## Results
{id: expect-random-and-regression-test-result}

```
~/work/training/testing/examples/bc>perl bc7.pl regress
```
![](examples/bc/bc7.pl.out)


## Expect multiple values
{id: expect-multiple-values}
![](examples/expect/random.pl)
![](examples/expect/random.t)


## Test::Expect
{id: expect-test-expect}
{i: Test::Expect}
{i: Expect::Simple}


* [Test::Expect](https://metacpan.org/pod/Test::Expect) by Leon Brocard is using
* [Expect::Simple](https://metacpan.org/pod/Expect::Simple) Diab Jerius which is a wrapper around Expect.


## Capturing both STDOUT and STDERR
{id: capturing-stdout-and-stderr}

* Write out the expected STDIN to a file called "in"
* Run the app    system "$app &lt; in >out 2>err";
* read in the out and err files an examine them



## Capturing both STDOUT and STDERR manually
{id: capturing-stdout-and-stderr-manually}
![](examples/io/capture.pl)


## Capturing both STDOUT and STDERR using IPC::Run3
{id: capturing-stdout-and-stderr-using-ipc-run3}
{i: IPC::Run3}
![](examples/io/capture_ipc.pl)


## Capture::Tiny
{id: capture-tiny}
{i: Capture::Tiny}
![](examples/perl/capture_tiny.pl)



## Test::Snapshots
{id: test-snapshots}
{i: Test::Snapshots}


[Test::Snapshots](https://metacpan.org/pod/Test::Snapshots).
Testing several command line-ish executables by saving INPUT,
command line ARGUMENTs expected OUTPUT, ERROR and EXIT code in external files.


```
bin/abc.exe

bin/abc.exe.in
bin/abc.exe.argv

bin/abc.exe.out
bin/abc.exe.err
bin/abc.exe.exit
```



## Exercise: Expect
{id: exercise-expect}


Take the bc6.pl example and similarly to bc7_diff.pl replace the way we compare data
to use [Test::Differences](https://metacpan.org/pod/Test::Differences).






