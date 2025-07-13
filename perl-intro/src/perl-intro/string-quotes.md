# single-quoted and double-quotes strings


```
$name    = 'Foo';
$message = "Hello $name, how are you?"; # Hello Foo, how are you?

$other   = 'Hello $name, how are you?'; # Hello $name, how are you?
```


```
print "\n";    # is a real newline
print '\n';    # will print \n
```

also use `q` or `qq`:


```
$message = qq{Hello $name, how are you?}; # Hello Foo, how are you?

$other   = q{Hello $name, how are you?}; # Hello $name, how are you?
```


