# Minimal Travis-CI installations


Even though the machine this runs on has a `minimal` installation it already has quite a few tools that you can use.
Instead of having a single value for the `script` key we convert it to a list of commands.
Travis executes all the other commands, but if any of these fails (has an exit code different from 0) then the whole process is reported as failure.

If they are all successful the it is reported as success.

You can see the detailed results in the console output.


{% embed include file="src/examples/minimal-installations/.travis.yml" %}

```
Release:	16.04
Codename:	xenial
```


