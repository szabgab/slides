# Hard coded path

In many application we can find hard-coded pathes. In order to test them we will need to create that exact path
which is not always easy. This also means we cannot run two tests at the same time with different content in those
files. (The actual "application" is just adding numbers together.)

{% embed include file="src/examples/exa/app.py" %}

{% embed include file="src/examples/exa/test_data_1.py" %}

pytest test_data_1.py

```
    def get_sum():
>       with open(data_file) as fh:
E       FileNotFoundError: [Errno 2] No such file or directory: '/corporate/fixed/path/data.json'
```


