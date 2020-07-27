# Web application development with Dancer
{id: dancer}

## Install Dancer2
{id: install-dancer}
{i: cpanm}
{i: Dancer2}

* Install [cpanm](https://metacpan.org/pod/App::cpanminus) if you don't have it yet: `curl -L https://cpanmin.us | perl - App::cpanminus`
* Install Dancer2: `cpanm Dancer2`

{aside}
Note, during the following pages I am going to use the word Dancer, however the name of the package we are using is Dancer2
and there is also a package called Dancer which was the first incarnation of this framework.
{/aside}

## Hello World with Dancer
{id: hello-world-with-dancer}
{i: get}
{i: plackup}
{i: to_app}
{i: psgi}

{aside}
Create an empty directory where you can put your files.

Create a file called `app.psgi` in that directory with the following content.

The `get` keyword creates a so-called route that maps a URL path onto an anonymous subroutine. In this
case we mapped the root page `/`.

Whatever the function returns will be returned to the browser. By default as HTML.

Then the `to_app` call basically provides a running application to `plack` which is a small web-server used for development purposes.
{/aside}

![](examples/dancer/hello_world/app.psgi)

* Run the application by `cd`-ing into its directory and then typing `plackup`
* Then you can see it at `http://localhost:5000`

{aside}
You might have noticed I did not add `use strict` and `use warnings` to this code.
That's because Dancer2 loads both of them by default.
{/aside}

## Testing Hello World of Dancer
{id: testing-hello-world-of-dancer}
{i: prove}
{i: Test::More}
{i: Plack::Test}
{i: HTTP::Request::Common}
{i: GET}
{i: done_testing}
{i: is}

{aside}
It is great that we can create a web page using Dancer, but if our application has any value to us
then we will want to make sure it works as expected and that it continues to work even after some changes were made.

The fastest and cheapest way to do this to write tests. Unit-, integration-, acceptance tests, name them as you like,
the important part is that they verify that the code works (and fails) as expected.

As this is such an integral part of writing code, we won't delay writing tests to the end of the project. We jump in right now.

Next to our `app.psgi` we create a file called `test.t` with the following content.
{/aside}

![](examples/dancer/hello_world/test.t)

{aside}
We can then run it by tping in `prove -v test.t` on the command line. this is going to be the output:
{/aside}

```
prove -v test.t
```

* [Test::More](https://metacpan.org/pod/Test::More)
* [Plack::Test](https://metacpan.org/pod/Plack::Test)
* [HTTP::Response](https://metacpan.org/pod/HTTP::Response)

![](examples/dancer/hello_world/test.out)

## Showing the current time with Dancer
{id: showing-the-current-time-with-dancer}

{aside}
In the first example we saw how to show a simple page that does not change between executions.

We now go a small step further and show a page that will show a different output every time we access it.

Still nothing fancy, just showing the current date and time.

We could of course use the built-in `time` function or the also built-in `localtime` function, but I wanted to
show something a bit nicer. So we are using the DateTime module to generate an object representing the current timestamp
and then we use the `strftime` method to create a nice-looking timestamp.

Dancer-wise we don't do much, we just return the resulting string.
{/aside}

![](examples/dancer/show_time/app.psgi)

* Run `plackup`
* Access at http://127.0.0.1:5000/
* Output: 2020-07-22 11:11:55

## Testing the current time with Dancer
{id: testing-the-current-time-with-dancer}
{i: like}
{i: qr}

{aside}
Just like in the first case, we would like to make sure our code works now and that it keeps working after we make
changes. So we are going to write a test for this application as well.

However unlike in the previous case, here we cannot compare the results to a fixed value as the result will be
different every time we run the test.

We could mock the time generating code of the Dancer application, but for this application it would be an overkill.

So instead of that we weaken our test and compare the results to a regular expression. So we don't know that the returned
string is indeed the correct date and time, but at least we can know that it looks like one.

The `like` keyword of Test::More provides this testing functionality.
{/aside}

![](examples/dancer/show_time/test.t)

* Run as `prove test.t`

## Process GET (query request) parameters in Dancer
{id: process-get-parameters-in-dancer}
{i: query_parameters}
{i: form}
{i: input}
{i: submit}

{aside}
Once we know how to generate responses on-the-fly, probably the next things we would like to know is how to handle user-input.
There are several ways to get input from a user of a web application. One of them is called query parameters that are sent
in via GET requests. You are probably familiar with them as they appear in the URL of a page after a question mark. Like this:

**echo?message=Foo+Bar**

Anyone could type in such a URL, but usually you have a HTML form on your page and when the user clicks on the submit button
then the browser sends in the data from the INPUT fields.

In our example the main route sends back a form with two INPUT elements. One of them is a text field the other one is the submit button.
In the FORM tag you can see the path to which the data of the form will be submitted along with the name of the method: GET. (The latter is
optional as GET is the default method.)

When the user visits the page, she will see an empty text box with a button that says "Echo". She can then type in some text
(e.g. **Foo Bar**), click on the button and the browser will submit the content by accessing the URL **echo?message=Foo+Bar**.

In the Dancer application this will trigger the '/echo' route where using the get method of the query_parameters object
we can receive the text sent in by the user. Then it is only a simple matter of sending it back to show what the user has typed in.
{/aside}

![](examples/dancer/get-parameters/app.psgi)

![](img/echo_form.png)

* Run as `plackup app.psgi` and then access at http://localhost:5000/


## Testing GET request with query parameters in Dancer
{id: testing-get-requests-with-query-parameters-in-dancer}


![](examples/dancer/get-parameters/test.t)


## Dancer: Get parameter in route
{id: get-param-in-route-dancer}
{i: param}
{i: subtest}

{aside}
Each URL path can be mapped to a specific function, but we can also map a whole set of URLs to a single function and use
parts of the URL path as parameters. For example we might want to show information about each user via their profile URL
which is **/user/ID** where the ID is their user id.
(For public URL it is probably a better idea is to let them have a unique username and use that, but the basic concept is the same.)

We can set it up in the following way:
{/aside}


![](examples/dancer/params-in-routes/app.psgi)

![](examples/dancer/params-in-routes/test.t)

## Dancer: Send 404 Not Found manually
{id: sent-404-not-found-manually-dancer}
{i: status}
{i: not_found}
{i: 404}

{aside}
If a user arrives to a URL path that is not associated with anything then Dancer will automatically return a 404 Not Found page.
What if we have a catch-all route as in the previous example, where one part of the URL path is the ID of a user.
What if then someone tries to access a page that does not belong to any user? Ideally the application would return a 404 Not Found page
this time as well, but Dancer cannot automatically understand which ID is valid and when to send a 404 Not found page.

We have to send it manually. For this, before sending back the page we first call `status 'not_found';` to tell Dancer to set the
HTTP return status to 404. Then we can send back any HTML (or plain text). It will be displayed but the browser, or whatever client
the user uses will be also told the status code is 404.
{/aside}


![](examples/dancer/return-404/app.psgi)

![](examples/dancer/return-404/test.t)

