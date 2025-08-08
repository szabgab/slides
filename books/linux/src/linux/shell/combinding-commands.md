# Combining commands

* The commnad **perldoc -lm Module::Name** will print the full path to the source code of a Perl Module.
* We can take that path and open with vim using:  **vim `perldoc -lm Module::Name`**.
* Maybe better this way: **vim $(perldoc -lm Module::Name)**.

