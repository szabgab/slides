# Remove from stage (unstage)


* unstage
* reset HEAD

```
$ git reset HEAD config.pl
```

```
Unstaged changes after reset:
M       README.txt
M       config.pl
```

```
$ git status
```
{% embed include file="src/examples/out/status_11.txt" %}


`$ git reset HEAD` will reset all the files currently staged.

See also the unstage alias we created earlier.


