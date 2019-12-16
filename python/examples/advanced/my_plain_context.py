from contextlib import contextmanager

@contextmanager
def my_plain_context():
   print("start context")
   yield
   print("end context")

with my_plain_context():
   print("In plain context")

