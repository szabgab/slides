# Flask: Run Hello World

* FLASK_DEBUG
* FLASK_APP
* run

In order to run this we need to set the environment variable **FLASK_APP** to the name of the file without the extension.
We can also set the **FLASK_DEBUG** environment variable to 1 tuning on the debug-mode, but this is not required for this example.

Then we execute `flask run`.

It is a bit different how you do this on Linux or Mac vs. on MS Windows.

In either case once flask is running you can use your browser to visit your new web application on http://127.0.0.1:5000/
You can also use `curl` on the command line to see the content of the web page.

Once you have enough, you can hit Ctr-C to stop the program.

Linux/Mac:

```
$ export FLASK_APP=app
$ export FLASK_DEBUG=1
$ flask run
```

or

```
FLASK_APP=app FLASK_DEBUG=1 flask run

Visit: http://127.0.0.1:5000/
curl http://localhost:5000/
```

Windows on the command line or in the terminal of Pycharm:

```
set FLASK_APP=app
set FLASK_DEBUG=1
flask run
```

Other parameters

```
$ FLASK_APP=echo.py FLASK_DEBUG=1  flask run --port 8080 --host 0.0.0.0
```

* To stop it use `Ctrl-C`


