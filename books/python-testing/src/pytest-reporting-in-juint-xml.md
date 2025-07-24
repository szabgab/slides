# Pytest reporting in JUnit XML format

* e.g. for Jenkins integration
* See [usage](https://docs.pytest.org/en/stable/usage.html)

```
pytest --junitxml report.xml
```

{% embed include file="src/examples/pytest/reporting/report.xml)

To make the XML more himan-readable:

```
cat report.xml | python -c 'import sys;import xml.dom.minidom;s=sys.stdin.read();print(xml.dom.minidom.parseString(s).toprettyxml())'
```


