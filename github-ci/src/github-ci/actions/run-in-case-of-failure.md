# Run in case of failure


{% embed include file="src/examples/workflows/in-case-of-failure.yml" %}

You can create a step that will run only if any of the previous steps failed.
In this example if you enable the "ls" statement in "Step one" it will fail
that will make Step two execute, but Step three won't because there was a failure.

On the other hand if Step One passes then Step Two won't run.
Step three will then run.

A failure in step three (e.g. by enabling the ls statement) will not make step Two run.


