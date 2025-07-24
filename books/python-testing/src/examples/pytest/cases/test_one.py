import logging

def add(x, y):
#    logger = logging.getLogger("mytest")
    logging.basicConfig(level = logging.INFO)
    logging.info("Just some info log")
    return x * y

def test_one():
    assert add(2, 2) == 4