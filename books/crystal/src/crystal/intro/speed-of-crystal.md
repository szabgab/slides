# Speed of Crystal

```
$ time crystal hello_world.cr
Hello World!

real  0m1.108s
user  0m1.268s
sys   0m0.271s
```

```
$ time crystal build hello_world.cr -o hw

real   0m1.108s
user   0m1.323s
sys    0m0.238s
```

```
$ time ./hw
Hello World!

real   0m0.013s
user   0m0.001s
sys    0m0.011s
```


