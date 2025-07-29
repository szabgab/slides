from contextlib import contextmanager

@contextmanager
def my_param_context(name):
   print(f"start {name}")
   yield
   print(f"end {name}")

with my_param_context("foo"):
   print("In param context")
