# Counting words - which implementation is faster?

* collections
* defaultdict
* Counter
* timeit
* try
* except

* In this example we have 4 functions counting the number of appearances of words that are already in memmory in a list.
* We use `timeit` to benchmark them.
* `repeat` is the number of repetition of each string.
* `different` is the number of different string.

{% embed include file="src/examples/perf/count_words_speed.py" %}
{% embed include file="src/examples/perf/count_words_speed.out" %}


