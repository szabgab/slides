# Signals
{id: signals}

## Signals and Python
{id: signals-and-python}
{i: kill}

* [man 7 signal](http://man7.org/linux/man-pages/man7/signal.7.html) (on Linux)
* Unix: kill PID, kill -9 PID, Ctrl-C, Ctrl-Z
* os.kill
* [signal](https://docs.python.org/library/signal.html)



## Sending Signal
{id: sending-signal}
{i: kill}

![](examples/signals/send_signal.py)

```
before
User defined signal 1: 30
```


## Catching Signal
{id: catching-signal}

![](examples/signals/catch_signal.py)

```
before
('Signal handler called with signal', 30)
after
```


## Catching Ctrl-C on Unix
{id: catching-ctrl-c-on-unix}

![](examples/signals/ctrl_c.py)

```
$  python ctrl_c.py
```
![](examples/signals/ctrl_c.out)


![](examples/signals/catch_ctrl_c.py)

* Cannot stop using Ctrl-C !
* Ctrl-Z and then kill %1
* kill PID


## Catching Ctrl-C on Unix confirm
{id: catching-ctrl-c-on-unix-confirm}

![](examples/signals/catch_ctrl_c_confirm.py)


## Alarm signal and timeouts
{id: alarm-signal}

![](examples/signals/alarm.py)

## Exercise: Catching Ctrl-C on Unix 2nd time
{id: exercise-catching-ctrl-c-on-unix-count}

* When Ctrl-C is pressed display: "In order to really kill the application press Ctrl-C again" and keep running. If the user presses Ctrl-C again, then let id die.
* Improve the previous that if 5 sec within the first Ctrl-C there is no 2nd Ctrl-C then any further Ctrl-C will trigger the above message again.


## Exercise: Signals
{id: exercise-signals}

* What signal is sent when you run **kill PID**?
* Write a script that will disable the **kill PID** for your process. How can you kill it then?
* What signal is sent when we press Ctrl-Z ?



## Ctrl-z
{id: ctrl-z}
![](examples/signals/kill_15.py)

```
kill PID
```

![](examples/signals/catch_kill_15.py)


