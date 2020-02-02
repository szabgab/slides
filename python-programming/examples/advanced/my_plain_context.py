from contextlib import contextmanager

@contextmanager
def my_plain_context():
    print("start context")
    yield
    print("end context")

print("START")
with my_plain_context():
    print("  In plain context")
    print("  More work")

print("END")
