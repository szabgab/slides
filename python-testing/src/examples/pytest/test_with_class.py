class TestClass():
    def test_one(self):
        print("one")
        assert True
        print("one after")

    def test_two(self):
        print("two")
        assert False
        print("two after")

class TestBad():
    def test_three(self):
        print("three")
        assert False
        print("three after")


