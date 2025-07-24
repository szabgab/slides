# Directories under t and prove


```
t/
  other.t
  something.t
  win32/
       ui.t
```

```
prove                   t/*.t
prove -r                recursively
prove t/something.t     t/something.t
prove t/win32           t/win32/*.t
```


If our test suite was setup as outlined above, even without a real perl module,
we can also keep the test files in a directory hierarchy under t/ - in that case we have
to indicate this in Makefile.PL or Build.PL. We can also run the tests script one-by-one
or per directory using the "prove" utility.



Let's see the layout of the sample CPAN packages we have, and run their tests:



By default "make test" or "perl Build test" will run all the t/*.t files.
Sometimes we want to run them one by one. We could run
**perl t/something.t** but that would try to use the installed
versions of the modules you are using and not those you are about to install.
So better use **perl -Ilib t/something.t** for that.

Even better to use the **prove t/something.t** command that comes with Test::More.
It too by default would attempt to use the already installed modules so you could run
**prove -b t/something.t** to include the files from blib/lib.
Prove has another frequently used flag: -v which puts it in verbose mode.



