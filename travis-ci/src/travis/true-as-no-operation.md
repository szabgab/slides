# true as no-operation to skip a step

* true

Sometimes, for some languages, there is some default behavior for the index and the script step but you'd like to skip that operation.
You can put `true` as the command to be executed. A a shell command the only thing it does is exit with success.

So you could write:

```
install: true
```


