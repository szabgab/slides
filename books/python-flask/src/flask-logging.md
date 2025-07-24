# Flask Logging


Logging is a very usefule tool to avoid the need for manual debugging. It also can provide insight as to what happened
in a session on the production server. During development you'll be able to see the messages on the terminal where Flask runs.
On the production server it can be saved in a log file for later review.

There are several pre-defined levels of logging. You can use the specific functions to indicate the importance of each log message.

You can set the level of logging inside the code or in an external configuration file.

{% embed include file="src/examples/flask/log/app.py" %}

