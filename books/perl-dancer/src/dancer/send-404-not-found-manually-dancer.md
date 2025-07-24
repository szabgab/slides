# Dancer: Send 404 Not Found manually


* status
* not_found
* 404


If a user arrives to a URL path that is not associated with anything then Dancer will automatically return a 404 Not Found page.
What if we have a catch-all route as in the previous example, where one part of the URL path is the ID of a user.
What if then someone tries to access a page that does not belong to any user? Ideally the application would return a 404 Not Found page
this time as well, but Dancer cannot automatically understand which ID is valid and when to send a 404 Not found page.

We have to send it manually. For this, before sending back the page we first call `status 'not_found';` to tell Dancer to set the
HTTP return status to 404. Then we can send back any HTML (or plain text). It will be displayed but the browser, or whatever client
the user uses will be also told the status code is 404.



{% embed include file="src/examples/dancer/return-404/app.psgi" %}



