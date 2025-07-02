# 500 Internal Server Error in Dancer



Mistakes can happen. There might be an exception somewhere in one of the routes. Don't worry though. If that happens Dancer will show a standard "500 Internal Error" page.

In our sample application the "/calc" route tries to make some calculation but a division by 0 error occures. This will trigger the "500 Internal Error".

Usually you don't plan to have certain URLs and certain input generate such error, so you probably will never write a test for this, but now, that we are showing it
I put together one.

Later we'll see how can we change the content of this page to be branded to our site.


{% embed include file="src/examples/dancer/hello_500/app.psgi" %}
{% embed include file="src/examples/dancer/hello_500/test.t" %}



