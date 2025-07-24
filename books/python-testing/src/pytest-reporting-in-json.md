# Pytest reporting in JSON format

* [pytest-json-report](https://pypi.org/project/pytest-json-report/)

```
pip install pytest-json-report

pytest --json-report --json-report-file=report.json --json-report-indent=4
```

Recommended to also add

```
--json-report-omit=log
```

```
pytest -s --json-report --json-report-file=report.json --log-cli-level=INFO
```


