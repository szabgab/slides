# Web Applications
{id: testing-web-applications}

## What can be tested ?
{id: web-applications-what-to-test}

* Fetching pages: type in a URL.
* Check if the HTML is correct.
* Check if elements of a page are in place.
* Follow links.
* Click on the link to the registration form, 
* Fill in the fields (you'll have to play with this and fill in the fields with good values, bad values, find the edge cases etc.)
* White box: Check if the changes also took place in the backend. (e.g. in the database.)
* Check if you get back the correct response page.
* ...



## Extreme web site testing
{id: manual-web-site-testing-extreme}

* Send data out of band, on lower level protocols, beneath the application.


{aside}

It is not enough to test the web application as it is. 
Users can actually send any request to your web server. 
Even if the client side part of your web application (written in HTML/CSS/Javascript )
behaves well, some people will try to send requests that would not be generated 
by your application. Sometimes that will happen by mistake - copy-pasting a URL
incorrectly. Sometime on purpose, when trying to attack your application.
{/aside}


If you want to seriously test your web application you'll have to do the same.
On the higher level protocols - you can send various http requests similar to
the valid ones, but with invalid data. You can also send invalid fields, and
you can try to attack your own application on low level protocols and send
invalid HTTP headers.





## Tools
{id: tools-testing-web-applications}

* [LWP::Simple](http://metacpan.org/pod/LWP::Simple)
* [LWP::UserAgent](http://metacpan.org/pod/LWP::UserAgent)
* [WWW::Mechanize](http://metacpan.org/pod/WWW::Mechanize) - based on the LWP library
* [Test::WWW::Mechanize](http://metacpan.org/pod/Test::WWW::Mechanize)
* [HTML::Lint](http://metacpan.org/pod/HTML::Lint)
* [Test::HTML::Lint](http://metacpan.org/pod/Test::HTML::Lint)
* [Test::HTML::Tidy](http://metacpan.org/pod/Test::HTML::Tidy)
* [Selenium](http://docs.seleniumhq.org/)



## Small test HTTP server
{id: test-http-server}


We are using a small portable HTTP server built using HTTP::Daemon
which is part of libwww-perl for the examples.




You can also run it by typing
<command>$ perl examples/www/server/server.pl</command>
or type the following to get help
<command>$ perl examples/www/server/server.pl --help</command>





## Fetching a static page
{id: fetching-static-page}
{i: LWP::Simple}
![](examples/www/static.t)

```
Fetch a page and check if there is response at all.
```

```
$ perl static.t          
1..1
ok 1 - There is a response
```


## Fetching a not-existing static page
{id: test-error-message}
![](examples/www/static_bad.t)

```
Fetch a page and check if there is response.
```

```
$ perl static_bad.t 
1..1
not ok 1 - There is a response
#     Failed test (static_bad.t at line 10)
# Looks like you failed 1 tests of 1.
```



## Checking good HTML
{id: html-lint-success}
{i: HTML::Lint}
{i: Test::HTML::Lint}
![](examples/www/static_lint.t)

```
$ perl static_lint.t 
1..2
ok 1 - There is a response
ok 2 - HTML OK
```


## Checking bad HTML
{id: html-lint-failor}
![](examples/www/static_lint_bad.t)

```
```
![](examples/www/static_lint_bad.t.out)


## What is this bad HTML ?
{id: bad-html}
![](examples/www/server/html/bad.html)


## HTML::Tidy and Test::HTML::Tidy
{id: test-html-tidy}
![](examples/www/static_tidy.t)


<command>$ perl examples/www/static_tidy.t</command>


![](examples/www/static_tidy.t.out)



## Test using W3C validator
{id: test-w3c}


<a href="http://validate.w3c.org/">W3C validator</a>



* Module to access that web site.
* Module to access the same service installed on a local web server.
* Module to access the validating code without a web server.



## Use a local copy of the W3C validator
{id: test-w3c-local}

```
On Ubuntu install the following packages using
sudo aptitude install w3c-dtd-xhtml w3c-linkchecker w3c-markup-validator

<command>dpkg -L w3c-markup-validator</command>
shows that the sample apache configuration file is at
/etc/w3c/w3c-markup-validator-apache-perl.conf
and the executable is at /usr/lib/cgi-bin/check

Change /etc/hosts w3c.local to resolve to 127.0.0.1

Copy the Apache configuration file and wrap it with a virtual host configuration.

Then access the page via http://w3c.local/w3c-markup-validator/
```
![](examples/www/w3c.conf)
![](examples/www/w3c_validate.pl)


## LWP::Simple and LWP
{id: lwp2}

```
LWP::Simple is, well, simple.

LWP on the other hand enables you to do a lot of things
```

* Setting the User Agent
* Support for cookies
* Authentication
* Proxy Servers
* Parse HTML
* Write robots


```
But is it not simple.
```



## WWW::Mechanize
{id: www-mechanize2}

```
Is simple, and very powerful (but does not support JavaScript).
```


## Web based Calculator with WWW::Mechanize
{id: www-mechanize-calculator}
![](examples/www/web_calc.pl)

Output:

![](examples/www/web_calc.pl.out)


## Testing with WWW::Mechanize
{id: testing-with-www-mechanize}
![](examples/www/web_calc.t)

```
Output:
```
![](examples/www/web_calc.t.out)


## Test::WWW::Mechanize
{id: test-www-mechanize}
![](examples/www/web_calc_test.t)

```
Output:
```
![](examples/www/web_calc_test.t.out)



## Login to Act using Mechanize
{id: act-mechanize}
![](examples/www/mechanize_act.pl)



## More things to test
{id: more-things-to-test}

* Check if you can access restricted pages without logging in ...
* or after logging out ...
* or after timeout expired
* logging-in, check good/bad passwords
* Upon unsuccessful login, see if the return page does NOT contain the password



## Test without server Test::WWW::Mechanize::PSGI
{id: test-www-mechanize-psgi}


<a href="https://metacpan.org/pod/Test::WWW::Mechanize::PSGI">Test::WWW::Mechanize::PSGI</a>



{aside}
PSGI-based applications can be tested without even launching a server.
{/aside}



## Test page with JavaScript
{id: test-javascript}
{i: WWW::Mechanize::Firefox}

* No single JavaScript engine, certainly there won't be those used in versions of IE
* There are several Open Source implementations
* Test only the data as it was sent
* Use a real browser (e.g. driven by [WWW::Mechanize::Firefox](https://metacpan.org/pod/WWW::Mechanize::Firefox) that needs [MozRepl](http://wiki.github.com/bard/mozrepl/) )
* Use Selenium






