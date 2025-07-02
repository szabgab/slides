# Process GET (query request) parameters in Dancer


* query_parameters
* GET
* form
* input
* submit


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

We are embedding the HTML in this code so it will be a one-file solution. In a bigger application we would use the template system and put the HTML in an external file.


{% embed include file="src/examples/dancer/get-parameters/app.psgi" %}

{% embed include file="src/img/echo_form.png)

* Run as `plackup app.psgi` and then access at http://localhost:5000/


