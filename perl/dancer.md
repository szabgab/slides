# Web application development with Dancer
{id: dancer}

## Install Dancer2
{id: install-dancer}
{i: cpanm}
{i: Dancer2}

* Install [cpanm](https://metacpan.org/pod/App::cpanminus) if you don't have it yet: `curl -L https://cpanmin.us | perl - App::cpanminus`
* Install Dancer2: `cpanm Dancer2`

{aside}
Note, during the following pages I am going to use the word Dancer, however the name of the package we are using is Dancer2
and there is also a package called Dancer which was the first incarnation of this framework.
{/aside}

## Hello World with Dancer
{id: hello-world-with-dancer}
{i: get}
{i: plackup}
{i: to_app}
{i: psgi}

{aside}
Create an empty directory where you can put your files.

Create a file called `app.psgi` in that directory with the following content.

The `get` keyword creates a so-called route that maps a URL path onto an anonymous subroutine. In this
case we mapped the root page `/`.

Whatever the function returns will be returned to the browser. By default as HTML.

Then the `to_app` call basically provides a running application to `plack` which is a small web-server used for development purposes.
{/aside}

![](examples/dancer/hello_world/app.psgi)

* Run the application by `cd`-ing into its directory and then typing `plackup`
* Then you can see it at `http://localhost:5000`

{aside}
You might have noticed I did not add `use strict` and `use warnings` to this code.
That's because Dancer2 loads both of them by default.
{/aside}

## Testing Hello World of Dancer
{id: testing-hello-world-of-dancer}
{i: prove}
{i: Test::More}
{i: Plack::Test}
{i: HTTP::Request::Common}
{i: GET}
{i: done_testing}
{i: is}

{aside}
It is great that we can create a web page using Dancer, but if our application has any value to us
then we will want to make sure it works as expected and that it continues to work even after some changes were made.

The fastest and cheapest way to do this to write tests. Unit-, integration-, acceptance tests, name them as you like,
the important part is that they verify that the code works (and fails) as expected.

As this is such an integral part of writing code, we won't delay writing tests to the end of the project. We jump in right now.

Next to our `app.psgi` we create a file called `test.t` with the following content.
{/aside}

![](examples/dancer/hello_world/test.t)

{aside}
We can then run it by tping in `prove -v test.t` on the command line. this is going to be the output:
{/aside}

```
prove -v test.t
```

* [Test::More](https://metacpan.org/pod/Test::More)
* [Plack::Test](https://metacpan.org/pod/Plack::Test)
* [HTTP::Response](https://metacpan.org/pod/HTTP::Response)

![](examples/dancer/hello_world/test.out)

## Showing the current time with Dancer
{id: showing-the-current-time-with-dancer}

{aside}
In the first exmple we saw how to show a simple page that does not change between executions.

We now go a small step further and show a page that will show a different output every time we access it.

Still noting fancy, just showing the current date and time.

We could of course use the built-in `time` function or the also built-in `localtime` function, but I wanted to
show something a bit nicer. So we are using the DateTime module to generate an object representing the current timestamp
and then we use the `strftime` method to create nice-looking timestamp.

Dancer-wise we don't do much, we just return the resulting string.
{/aside}

![](examples/dancer/show_time/app.psgi)

* Run `plackup`
* Access at http://127.0.0.1:5000/
* Output: 2020-07-22 11:11:55

## Testing the current time with Dancer
{id: testing-the-current-time-with-dancer}
{i: like}
{i: qr}

{aside}
Just like in the first case, we would like to make sure our code works now and that it keeps working after we make
changes. So we are going to write a test for this application as well.

However unlike in the previous case, here we cannot compare the results to a fixed value as the result will be
different every time we run the test.

We could mock the time generating code of the Dancer application, but for this application it would be an overkill.

So instead of that we weaken our test and compare the results to a regular expression. So we don't know that the returned
string is indeed the correct date and time, but at least we can know that it looks like one.

The `like` keyword of Test::More provides this testing functionality.
{/aside}

![](examples/dancer/show_time/test.t)

* Run as `prove test.t`

