# Dancer: Type-checking for the route parameters


* Int


Dancer allows us to use type-constraints to limit what values we accept in a route. For example we can tell it that the value must be an integer.

If the request does not match the expected type then that route does not match. If none of the routes match then we get a "404 Not Found" error as expected.


* [Route-Handlers](https://metacpan.org/pod/distribution/Dancer2/lib/Dancer2/Manual.pod#Route-Handlers)
* [Types](https://metacpan.org/pod/distribution/Type-Tiny/lib/Type/Tiny/Manual/AllTypes.pod)

{% embed include file="src/examples/dancer/params-in-routes-int/app.psgi" %}



