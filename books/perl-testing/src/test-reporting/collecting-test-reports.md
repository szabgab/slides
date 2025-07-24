# Collecting Test reports

Collect the report with the following command:

```
prove -b -a tap.tar.gz  examples/tap
```

and save it on a centralized server.


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



