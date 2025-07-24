# Dancer: Receive parameter in route

* param
* subtest


Each URL path can be mapped to a specific function, but we can also map a whole set of URLs to a single function and use
parts of the URL path as parameters. For example we might want to show information about each user via their profile URL
which is **/user/ID** where the ID is their user id.
(For public URL it is probably a better idea to let them have a unique username and use that, but the basic concept is the same.)

We can set it up in the following way:



{% embed include file="src/examples/dancer/params-in-routes/app.psgi" %}



