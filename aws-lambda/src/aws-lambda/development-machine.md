# Development machine

* [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance)
* Using [pylev](https://pypi.org/project/pylev/) which is pure Python.


{% embed include file="src/examples/app_pylev/lambda_function.py" %}

```
mkdir app_pylev
cd app_pylev
pip install pylev -t pypi
zip -r ../project.zip *
```

* `curl 'https://qspmdah6oj.execute-api.us-east-1.amazonaws.com/v0/hello?a=abd&b=acx'`



