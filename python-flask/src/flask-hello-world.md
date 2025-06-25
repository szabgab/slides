# Flask: Hello World

* Flask
* route
* app

The de-facto standard first thing to do in programming in every language or framework is to print "Hello World" on the screen.
This is what we are going to do with Flask now. This is probably the most simple Flask application.

For this we need to create regular Python file, for example **app.py**. I'd recommend you first create a new empty directory and
put the file inside that directory.

The first thing is to load the **Flask** class from the **flask** module.

Then we create an object representing the whole application. You could use any variable name for this, but the "standard" is to use
the name **app**.

Then comes the interesting part. We declare a function that will return the HTML page.
In our example the name of the function is **main**, but the name actually is not important. You could as well call it **some_other_name**.
The important part is the decorator above it. That decorator means that if someone reaches the path `/` on the web site, this function will
be executed and whatever it returns will be sent back to the browser. This mapping of a path to a function is called URL **routing** and we'll
discuss it in detail later on.

For now, let's see how we can use this.


{% embed include file="src/examples/flask/hello_world/app.py" %}



