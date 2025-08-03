# Exit early with exit code

* Exit
* os.Exit
* %ERRORLEVEL%
* $?


In the earlier examples our code stopped running when the last statement in the main function was executed.
This is usually the normal way for your code to end, but there can be various circumstances when you want your program to
stop running even before it reaches the last statement. You can do this by calling the `os.Exit()` function.

You will also have to pass a number to this function which is going to be the exit-code of your program.
If you did not explicitly call `os.Exit()` then go will automatically set the exit-code to be 0. That means success.

In general exit-code 0 means success. Any other number indicates failure. Which number indicates which failure is totally up to
you as a programmer.

The exit code is not printed anywhere on the screen, it is sort-of invisible, but the user of your program can check it by looking at
the value of the `$?` variable on Unix/Linux/Mac systems, or the `%ERRORLEVEL%` variable on MS Windows systems.


{% embed include file="src/examples/exit/code.go" %}

```
echo $0
echo %ERRORLEVEL%
```


