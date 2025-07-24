import app
import time

def test_one():
    our_real_1 = time.time()
    their_real_1 = app.now()
    assert abs(our_real_1 - their_real_1) < 0.00001

    app.time.time = lambda : our_real_1 + 100

    our_real_2 = time.time()
    print (our_real_2 - our_real_1)
    #their_real_2 = app.now()
    #assert abs(our_real_2 - their_real_2) >= 100


