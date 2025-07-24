import datetime
import time

def test_datetime(monkeypatch):
    assert datetime._time == time
