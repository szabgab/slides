# Local storage - boolean

* JSON


In many browsers local storage can only store string. So when we store the boolean true or false, it actually stores
the strings "true" or "false". In order to get back the real boolean values, we can use the JSON.parse() method.

{% embed include file="src/examples/js/local_storage_boolean.html" %}


