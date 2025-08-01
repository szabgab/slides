# Async chores

* async
* await


{% embed include file="src/examples/async/async_chores.py" %}

From the output you can see that we noticed that the washing machine has finished only after we
have finished all the potatoes. That's becasue our potato cleaning process was a long-running
CPU-intensive process. This means the dryer only starts working after the potatoes are clean.

{% embed include file="src/examples/async/async_chores.out" %}

If after cleaning each potato we look up for a fraction of a second, if we let the main loop run,
then we can notice that the washing machine has ended and we can turn on the dryer before continuing
with the next potato. This will allow the dryer to work while we are still cleaning the potatoes.

{% embed include file="src/examples/async/async_chores_async.out" %}


