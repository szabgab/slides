# Drop local changes (restore to HEAD or to index)

* restore
* checkout

```
$ git restore config.pl
$ git checkout config.pl    # old school :-)
$ git status
```

`git checkout FILENAME`
will replace FILENAME in the work tree with the one committed (or if there is a version already staged then to that version).
You loose your local work.


`git checkout .` will do it for all the files in the tree.

{% embed include file="src/examples/out/status_12.txt" %}


