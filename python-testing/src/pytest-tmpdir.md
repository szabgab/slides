# Pytest fixture - tmpdir

* tmpdir

* Probably the simples fixture that PyTest can provide is the `tmpdir`.
* Pytest will prepare a temporary directory and call the test function passing the path to the `tmpdir`.
* PyTest will also clean up the temporary folder, though it will keep the 3 most recent ones. (this is configurable)

{% embed include file="src/examples/pytest/test_tmpdir.py" %}

