# Pytest: expect a test to fail (xfail or TODO tests)

```
$ pytest test_mymod_3.py
```

```
======= test session starts =======
platform darwin -- Python 3.5.2, pytest-3.0.7, py-1.4.33, pluggy-0.4.0
Using --random-order-bucket=module
Using --random-order-seed=557111

rootdir: /Users/gabor/work/training/python/examples/pytest, inifile:
plugins: xdist-1.16.0, random-order-0.5.4
collected 2 items

test_mymod_3.py .x

===== 1 passed, 1 xfailed in 0.08 seconds =====
```



