# Can module be loaded? use_ok and require_ok

* use_ok
* require_ok



use_ok and require_ok are not recommended any more. Just **use** or **require** the modules as necessary
and let perl provide the appropriate failure message if either of those fails.

{% embed include file="src/examples/test-perl/t/use_ok.t" %}

```
1..1
ok 1 - use MyTools;
```


