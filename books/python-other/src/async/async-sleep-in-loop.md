# Async sleep in loop

* create_task

* 4 sleeping in parallel will be much faster
* This time we used `create_task` to set up the tasks ahead of time and the we awaited all of them.

{% embed include file="src/examples/async/sleep_loop_async.py" %}
{% embed include file="src/examples/async/sleep_loop_async.out" %}


