# Sync chores

We have a number of household chores to do. Each takes a couple of seconds for a machine to do
while we have time to do something else. We also have one task, cleaning potatoes, that requires
our full attention. It is a CPU-intensive process.

We also have two processes depending each other. We can turn on the dryer only after the
washing machine has finished.

{% embed include file="src/examples/async/sync_chores.py" %}
{% embed include file="src/examples/async/sync_chores.out" %}


