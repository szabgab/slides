# Solution: Calculator eval



{% embed include file="src/examples/basics/calculator_eval.py" %}

```
$ python examples/basics/calculator_eval.py

Number: 2
Number: 3
Operator (+-*/): +
2+3
5
```

Try Again, this time:

```
$ python examples/basics/calculator_eval.py

Number: os.system("ls -l")
Number:
Operator (+-*/):
```

And then you could try it with `rm -rf /` or if you are on Windows try `os.system("dir")`
or this: `os.system("rm -f calculator_eval.py")` and on windows it would be `os.system("del calculator_eval.py")`.


* Now forget this and don't use `eval` for the next few years!


