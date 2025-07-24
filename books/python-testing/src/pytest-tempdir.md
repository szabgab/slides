# Pytest and tempdir

* tmpdir

* This is a simple application that reads and writes config files (ini file).
* We can test the `parse_file` by preparing some input files and check if we get the expected data structure.
* In order to test the `save_file` we need to be able to save a file somewhere.
* Saving it in the current folder will create garbage files. (and the folder might be read-only in some environments).
* For each test we'll have to come up with a separate filename so they won't collide.
* Using a `tmpdir` solves this problem.

{% embed include file="src/examples/pytest/mycfg.py" %}
{% embed include file="src/examples/pytest/a.cfg)
{% embed include file="src/examples/pytest/test_mycfg.py" %}



