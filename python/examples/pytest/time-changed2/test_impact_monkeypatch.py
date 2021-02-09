import app
import time

def test_one(monkeypatch):
    our_real_1 = time.time()
    their_real_1 = app.now()
    assert abs(our_real_1 - their_real_1) < 0.0001

    monkeypatch.setattr(app, 'time', lambda : our_real_1 + 100)

    our_real_2 = time.time()
    assert abs(our_real_2 - our_real_1) < 0.0001

    their_real_2 = app.now()
    assert abs(our_real_2 - their_real_2) >= 99

def test_two():
    our_real_1 = time.time()
    their_real_1 = app.now()
    assert abs(our_real_1 - their_real_1) < 0.00001


