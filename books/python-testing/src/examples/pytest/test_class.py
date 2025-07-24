class TestClass():
    def setup_class(self):
        print("setup_class called once for the class")
        print(self)
        self.db = "mydb"
        self.test_counter = 0

    def teardown_class(self):
        print(f"teardown_class called once for the class {self.db}")

    def setup_method(self):
        self.test_counter += 1
        print(f"  setup_method called for every method {self.db} {self.test_counter}")
        print(self)

    def teardown_method(self):
        print(f"  teardown_method called for every method {self.test_counter}")


    def test_one(self):
        print("    one")
        assert True
        print("    one after")

    def test_two(self):
        print("    two")
        assert False
        print("    two after")

    def test_three(self):
        print("    three")
        assert True
        print("    three after")
