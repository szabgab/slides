# Jinja extend template layout block


* layout
* extends
* block

We use **extend** to connect between templates.
We use **block** both to mark the area that will be replaced and the content that will replace it.

{% embed include file="src/examples/flask/template-extends/app.py" %}
{% embed include file="src/examples/flask/template-extends/test_app.py" %}
{% embed include file="src/examples/flask/template-extends/templates/index.html" %}
{% embed include file="src/examples/flask/template-extends/templates/layouts/base.html" %}

