# Program name

* PROGRAM_NAME

{% embed include file="src/examples/intro/program_name.cr" %}

* When running with `crystal examples/intro/program_name.cr`:

{% embed include file="src/examples/intro/program_name.out" %}

We can also compile it

```
crystal build examples/intro/program_name.cr
```

* This will generate `program_name` (as that was the name of our source file)
* We can rename it: `mv program_name other`
* We can run it `./other` and it will print the name of the executable file `other`.


* [See other top-level variables](https://crystal-lang.org/api/toplevel.html)



