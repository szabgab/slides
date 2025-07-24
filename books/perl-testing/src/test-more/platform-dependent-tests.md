# Platform dependent tests


{% embed include file="src/examples/test-more/t/without_skip.t" %}

{% embed include file="src/examples/test-more/t/without_skip.t.out" %}


Sometimes, you know that a part of your test suite isn't relevant.
Running them - if at all possible - would report false results.
Maybe some of the features of your system are platform dependent, you don't want to
test them on an unsupported platform. Sometimes failure of previous tests make a
test irrelevant.

In all such cases what you actually want is to skip the tests. Surprisingly the way
to do that is to enclose the tests in a SKIP block.



