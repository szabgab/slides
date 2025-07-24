# Debugging a failed request



In the previous example you saw that I had to set `:use_ssl => true`, but it took some time to figure it out.
The main problem was that in case of failure my previous code only printed the HTTP status code that was 400.

I read the documentation several times and tried various combinations of the code till it occurred to be that maybe
there is some hint in the `body` of the response. So I changed the code to print that in case of failure.


{% embed include file="src/examples/net-http/post_header_httpbin.rb" %}

This was the response:

{% embed include file="src/examples/net-http/post_header_httpbin.out" %}

That allowed me to understand that the issue is around the use of ssl: http vs https. First I tried the same code
replacing the URL by one that uses http:

```
url = 'http://httpbin.org/post'
```

This worked.

At this point I understood I need to search for something about ssl, and that's how I found out that I had to pass `:use_ssl => true`.

So remember, at least for debugging, it can be useful to print the content of the body even in the case of error.



