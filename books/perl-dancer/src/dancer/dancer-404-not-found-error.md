# 404 Not Found in Dancer

If a user tries to access a path that has no matching route defined then Dancer will return a default "404 Not Found" error page
with the appropriate HTTP status code.

Later we'll see how can we change the content of this page to be branded to our site.


{% embed include file="src/examples/dancer/hello_404/app.psgi" %}
{% embed include file="src/examples/dancer/hello_404/test.t" %}


