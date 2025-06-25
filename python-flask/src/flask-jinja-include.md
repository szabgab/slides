# Flask Jinja include



```
.
├── app.py
├── test_app.py
└── templates
    ├── incl
    │   ├── footer.html
    │   └── header.html
    └── main.html
```

{% embed include file="src/examples/flask/jinja-include/app.py" %}
{% embed include file="src/examples/flask/jinja-include/templates/main.html" %}
{% embed include file="src/examples/flask/jinja-include/templates/incl/header.html" %}
{% embed include file="src/examples/flask/jinja-include/templates/incl/footer.html" %}

{% embed include file="src/examples/flask/jinja-include/test_app.py" %}

