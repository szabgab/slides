# Process POST requests in Dancer


* body_parameters
* POST


In addition to the GET request the other common verb used in HTTP is POST. When you are implementing a REST API these verbs have real meaning,
but when you are writing a user-facing web application the choice between GET and POST usually boils down to the question if you'd like
the people to see the parameters passing in the URL or not.

With GET you'd have the visible query string, with POST the browser will send the same data in the body of the HTTP request invisible to
the regular user. The data is still sent and if the server does not use https, the data is still readable by anyone listening on the wire.

You probably use GET if you'd like to allow your users to send the specific URL with the data to someone else or if you'd like to let them
bookmark the page with the data. You'd use POST if you prefer they don't send the data to their friends as well.

In the code we had to make the following changes:

On the main page the form now sets the method to be POST.

The /echo route is now declared with the `post` keyword telling Dancer to execute this function when a POST request arrives at that route.

The data is extracted from the request in the `body_parameters` hash.


{% embed include file="src/examples/dancer/post-parameters/app.psgi" %}

* Run as `plackup app.psgi` and then access at http://localhost:5000/


