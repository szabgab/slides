# Common error messages

* undef

```
Global symbol "$x" requires explicit package name at ..
```


You need to declare the variable $x by `my`.



```
Use of uninitialized value $x in ... at ...
```


$x contained `undef`.



```
Name "main::x" used only once: possible typo at ...
```


What it said. It probably refers to $x.



```
Can't locate Module/NameX.pm in @INC (@INC contains: ... )
```


You probably have "use Module::NameX" in your code meaning you are trying to load
Module::NameX. Either there is a typo in the name of the module (e.g. in our case it is
probably called Module::Name) or you need to install Module::NameX.



```
Scalar found where operator expected at ...
```


Probably a , is missing between parameters of a function?



* [Common Warnings and Error messages in Perl](https://perlmaven.com/common-warnings-and-error-messages)




