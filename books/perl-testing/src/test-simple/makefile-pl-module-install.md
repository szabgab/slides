# Makefile.PL for Module::Install

Makefile.PL
Module::Install

{% embed include file="src/examples/distribution/project_with_module_install/Makefile.PL" %}


In Module::Install the declaration is cleaner and it does not need to be
installed on the target machine. When running perl Makefile.PL it creates
and inc subdirectory and copies itself there. One should distribute
this directory as well.



On the target system Module::Install is loaded from this subdirectory.


```
$ perl Makefile.PL
$ make
$ make test
```

```
$ make manifest
$ make dist
```



