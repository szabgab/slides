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

