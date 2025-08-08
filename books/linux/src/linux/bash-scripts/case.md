# case

* case
* esac

{% embed include file="src/examples/script/case.sh" %}

```
$ ./examples/script/case.sh foo
it is foo

$ ./examples/script/case.sh abc
letters

$ ./examples/script/case.sh 123
digits

$ ./examples/script/case.sh 42
digits

$ ./examples/script/case.sh 
default

$ ./examples/script/case.sh abc123
letters
```

* ;;      - no subsequent cases are checked
* ;&amp;  - execute the subsequent blocks until ;; is found or till the esac.
* ;;&amp; - check the subsequent condition till you find a match.








