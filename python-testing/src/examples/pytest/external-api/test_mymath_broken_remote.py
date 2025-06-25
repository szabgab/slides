import mymath

def mocked_remote_compute(x):
    if x == 3:
        return '9'
    if x == 4:
        return 16

mymath.externalapi.remote_compute = mocked_remote_compute

# What should we really expect here?
# I don't want to see a Python-level exception
# Maybe an exception of our own.
def test_compute_breaks():
    assert mymath.compute(3, 4) == 5
