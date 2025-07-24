# PyTest test discovery

Running pytest will find test files and in the files test functions.


* test_*.py files
* *_test.py files
* test_*  functions
* TestSomething class
*   test_* methods

```
examples/pytest/discovery
.
├── db
│   └── test_db.py
├── other_file.py
├── test_one.py
└── two_test.py

```

{% embed include file="src/examples/pytest/discovery.out" %}



