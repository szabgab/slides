# Showing the current time with Dancer



In the first example we saw how to show a simple page that does not change between executions.

We now go a small step further and show a page that will show a different output every time we access it.

Still nothing fancy, just showing the current date and time.

We could of course use the built-in `time` function or the also built-in `localtime` function, but I wanted to
show something a bit nicer. So we are using the DateTime module to generate an object representing the current timestamp
and then we use the `strftime` method to create a nice-looking timestamp.

Dancer-wise we don't do much, we just return the resulting string.


{% embed include file="src/examples/dancer/show_time/app.psgi" %}

* Run `plackup`
* Access at http://127.0.0.1:5000/
* Output: 2020-07-22 11:11:55


