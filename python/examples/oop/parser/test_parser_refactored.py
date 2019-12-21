from parser_refactored import parse
import json

def test_dom():
    dom = parse('text.md')
    with open('text.json') as fh:
        expected = json.load(fh)
    assert dom == expected

