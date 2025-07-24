# Mocking function of external web call

* Test::Mock::Simple

* We have an application that uses LWP::Simple
* It gets a list of strings and tells us how many times each string appears on that web page.
* We'll talk about the commented out code a bit later.

{% embed include file="src/examples/mock-lwp/lib/MyWebAPI.pm" %}

{% embed include file="src/examples/mock-lwp/bin/count.pl" %}

```
perl -Ilib bin/count.pl https://code-maven.com/ perl python Java
```


