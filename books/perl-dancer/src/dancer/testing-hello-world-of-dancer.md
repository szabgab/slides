# Testing Hello World of Dancer


* prove
* Test::More
* Plack::Test
* HTTP::Request::Common
* GET
* done_testing
* is


It is great that we can create a web page using Dancer, but if our application has any value to us
then we will want to make sure it works as expected and that it continues to work even after some changes were made.

The fastest and cheapest way to do this to write tests. Unit-, integration-, acceptance tests, name them as you like,
the important part is that they verify that the code works (and fails) as expected.

As this is such an integral part of writing code, we won't delay writing tests to the end of the project. We jump in right now.

Next to our `app.psgi` we create a file called `test.t` with the following content.


{% embed include file="src/examples/dancer/hello_world/test.t" %}


We can then run it by typing in `prove -v test.t` on the command line. this is going to be the output:


```
prove -v test.t
```

* [Test::More](https://metacpan.org/pod/Test::More)
* [Plack::Test](https://metacpan.org/pod/Plack::Test)
* [Plack::Util](https://metacpan.org/pod/Plack::Util)
* [HTTP::Response](https://metacpan.org/pod/HTTP::Response)

{% embed include file="src/examples/dancer/hello_world/test.out" %}


