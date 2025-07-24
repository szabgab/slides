# Hello World with Dancer


* get
* plackup
* to_app
* psgi


Create an empty directory where you can put your files.

Create a file called `app.psgi` in that directory with the following content.

The `get` keyword creates a so-called route that maps a URL path onto an anonymous subroutine. In this
case we mapped the root page `/`.

Whatever the function returns will be returned to the browser. By default as HTML.

Then the `to_app` call basically provides a running application to `plack` which is a small web-server used for development purposes.


{% embed include file="src/examples/dancer/hello_world/app.psgi" %}

* Run the application by `cd`-ing into its directory and then typing: **plackup**
* Then you can see it at **http://localhost:5000**


You might have noticed I did not add `use strict` and `use warnings` to this code.
That's because Dancer2 loads both of them by default.


