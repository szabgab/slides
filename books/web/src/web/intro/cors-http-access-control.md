# HTTP Access Control (CORS)

```
XMLHttpRequest cannot load http://127.0.0.1:5000/api/v1/greeting.
No 'Access-Control-Allow-Origin' header is present on the requested resource.
Origin 'null' is therefore not allowed access.
```

lib/D2/Ajax.pm


```
header 'Access-Control-Allow-Origin' => '*';
```

Let's create v2 of the API

{% embed include file="src/examples/snippets/2/lib/D2/Ajax.pm" %}

Try: [v2](file:///Users/gabor/work/D2-Ajax/client/v2.html" %}





