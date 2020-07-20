# Web application development with Dancer
{id: dancer}

## Install Dancer2
{id: install-dancer}

* Install [cpanm](https://metacpan.org/pod/App::cpanminus) if you don't have it yet: `curl -L https://cpanmin.us | perl - App::cpanminus`
* Install Dancer2: `cpanm Dancer2`

{aside}
Note, during the following pages I am going to use the word Dancer, however the name of the package we are using is Dancer2
and there is also a package called Dancer which was the first incarnation of this framework.
{/aside}

## Hello World with Dancer
{id: hello-world-with-dancer}

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


## Testing Hello World of Dancer
{id: testing-hello-world-of-dancer}

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

* [Plack::Test](https://metacpan.org/pod/Plack::Test)
* [HTTP::Response](https://metacpan.org/pod/HTTP::Response)

![](examples/dancer/hello_world/test.out)

