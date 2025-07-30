# ctypes - hello

* ctypes

{% embed include file="src/examples/c/hello.c" %}

```
gcc -o hello hello.c
gcc -o hello.so -shared -fPIC hello.c
```

{% embed include file="src/examples/c/hello.py" %}


