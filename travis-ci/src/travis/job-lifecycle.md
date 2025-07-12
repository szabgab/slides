# Job Lifecycle


* Defaults for each language

{% embed include file="src/examples/lifecycle/.travis.yml" %}

```
$ echo "Before install"
$ echo "Install"
$ echo "Before the script phase"
$ echo "The main task"
$ echo "After success"
$ echo "After the script phase."
```

* Add a `- ls qqrq` to the steps to see how we get the "After failure" message.


