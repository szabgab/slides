# Solution: Web client


{% embed include file="src/examples/web_client/lambda_function.py" %}

{% embed include file="src/examples/web_client/requirements.txt)

{% embed include file="src/examples/web_client/setup.cfg)

```
pip install -r requirements.txt -t pypi
zip -r ../project.zip *
```

```
curl 'https://qspmdah6oj.execute-api.us-east-1.amazonaws.com/v0/hello?url=https://httpbin.org/get'
```


