# splain and use diagnostics

* splain
* diagnostics

```
perl examples/advanced-perl/code_with_warnings.pl 2> err.txt
splain err.txt
```

The output looks like this:

```
Use of uninitialized value $total in addition (+) at
	examples/advanced-perl/use_diagnostics.pl line 15 (#1)
    (W uninitialized) An undefined value was used as if it were already
    defined.  It was interpreted as a "" or a 0, but maybe it was a mistake.
    To suppress this warning assign a defined value to your variables.

    To help you figure out what was undefined, perl will try to tell you the
    name of the variable (if any) that was undefined. In some cases it cannot
    do this, so it also tells you what operation you used the undefined value
    in.  Note, however, that perl optimizes your program and the operation
    displayed in the warning may not necessarily appear literally in your
    program.  For example, "that $foo" is usually optimized into "that "
    . $foo, and the warning will refer to the concatenation (.) operator,
    even though there is no . in your program.
```


Alternatively you could also insert the following in your code:
`use diagnostics;`
to get the explanations for every warning.
See also `perldoc perldiag` for a detailed explanation of each warning and error.


