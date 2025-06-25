# Flask: Echo GET

* request
* request.args

request.args is a dictionary. We could write request.args['name'] but then it would raise and excpetion and the whole application would crash
if the user did not send in a value for the "name" field. We could check if the key exists before trying to access the value using the "in" operator,
but that seems like a bit of a waste of work here. Instead we call the "get" method that every dictionary in Python has. It will return None, if the key "name"
did not exists. We could even provide a default value to the "get" method".


{% embed include file="src/examples/flask/echo_get/app.py" %}

