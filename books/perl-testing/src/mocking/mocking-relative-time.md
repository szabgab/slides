# Mocking relative Time

* Test::MockTime
* time

* [Test::MockTime](https://metacpan.org/pod/Test::MockTime)

{% embed include file="src/examples/mock-elapsed-time/t/time.t" %}


Make sure you load Test::MockTime before you load the module under testing. Otherwise the time function in that module won't be mocked.


