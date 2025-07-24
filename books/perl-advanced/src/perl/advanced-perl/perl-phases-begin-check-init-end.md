# Compilation phases: BEGIN, CHECK, INIT, END

* BEGIN
* CHECK
* INIT
* END

```
BEGIN {
    # do something here
}
```

```
* You can have more than one of each one

BEGIN  - execute as soon as possible (compiled)
CHECK  - execute after the whole script was compiled
INIT   - execute before running starts
END    - execute as late as possible (after exit() or die())

When running perl -c script.pl   both the BEGIN and CHECK blocks are executed.

perldoc perlmod
```
{% embed include file="src/examples/advanced-perl/begin_end.pl" %}
{% embed include file="src/examples/advanced-perl/begin_end.out" %}
{% embed include file="src/examples/advanced-perl/phases.pl" %}
{% embed include file="src/examples/advanced-perl/phases.out" %}



