# Multitasking
{id: multitasking}

## What is Multitasking?
{id: what-is-multitasking}

* [Multitasking](https://pypi.org/project/multitasking/)
* A wrapper around threading and os.fork by Ran Aroussi

```
pip install multitasking
```

## Multitasking example
{id: multitasking-example}
{i: multitasking}
{i: task}
{i: set_max_threads}

![](examples/multitasking/example.py)
![](examples/multitasking/example.out)

## Multitasking example with wait
{id: multitasking-example-with-wait}
{i: wait_for_tasks}

![](examples/multitasking/example_with_wait.py)
![](examples/multitasking/example_with_wait.out)

## Multitaksing - second loop waits for first one
{id: multitaksing-two-loops}

[](examples/multitasking/two_loops.py)

## Multitasking counter
{id: multitasking-counter}

[](examples/multitasking/counter.py)
[](examples/multitasking/counter.out)

## Multitasking counter with thread locking
{id: multitasking-counter-with-locking}
{i: threading}
{i: Lock}
{i: acquire}
{i: release}

[](examples/multitasking/counter_with_locking.py)
[](examples/multitasking/counter_with_locking.out)

