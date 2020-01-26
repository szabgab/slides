import os
import json
import pytest

from packets import Packets

root = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(root, 'packets.json')) as fh:
    expected_results = json.load(fh)

@pytest.mark.parametrize('filename', ['packets.txt', 'packets1.txt', 'packets2.txt'])
def test_packetes(filename):
    filepath = os.path.join(root, filename)

    results = []
    for packet in Packets(filepath):
        results.append(packet)
    assert results == expected_results

