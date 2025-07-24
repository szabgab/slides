# cmp_ok(   this,   op,  that,    name);


* cmp_ok



Sometimes an eq by is() or a regular expression by like() just isn't good enough.
For example what if you would like to check the rand() function of perl? Its result 
must be between 0 (inclusive) and 1 (non inclusive).



In other case you might have a function that should happen within a certain period of time.
You don't have an exact expectation but you know the elapsed time must be between a lower
and upper limit.


`cmp_ok` compares with any operator you like.

{% embed include file="src/examples/test-more/t/cmp_ok.t" %}

{% embed include file="src/examples/test-more/t/cmp_ok.t.out" %}

{% embed include file="src/examples/test-more/t/cmp_ok.t.2.out" %}

* Actually this is a really bad test as it can fail randomnly


