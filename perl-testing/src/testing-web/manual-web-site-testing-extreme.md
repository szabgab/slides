# Extreme web site testing


* Send data out of band, on lower level protocols, beneath the application.

It is not enough to test the web application as it is.
Users can actually send any request to your web server.
Even if the client side part of your web application (written in HTML/CSS/Javascript )
behaves well, some people will try to send requests that would not be generated
by your application. Sometimes that will happen by mistake - copy-pasting a URL
incorrectly. Sometime on purpose, when trying to attack your application.



If you want to seriously test your web application you'll have to do the same.
On the higher level protocols - you can send various http requests similar to
the valid ones, but with invalid data. You can also send invalid fields, and
you can try to attack your own application on low level protocols and send
invalid HTTP headers.


