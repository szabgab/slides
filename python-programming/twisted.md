# Asynchronus programming with Twisted
{id: python-twisted}

## About Twisted
{id: about-twisted}

* [Twisted](https://twistedmatrix.com/)


## Echo
{id: echo}

![](examples/twisted/echoserver.py)
![](examples/twisted/echoclient.py)


## Echo with log
{id: echo-with-log}

![](examples/twisted/echoserver_log.py)


## Simple web client
{id: simple-web-client}

The code behind this example was deprecated. Need to be fixed.

* getPage() returns a "deferred"
* addCallbacks(on_success, on_failure)
* addBoth(on_both)   adds callbock to both success and failure callback chain

![](examples/twisted/simple_web_client.py)


## Web client
{id: web-client}

![](examples/twisted/web_client.py)


