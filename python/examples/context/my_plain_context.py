from contextlib import contextmanager
import sys

param = ''
if len(sys.argv) == 2:
    #exit(f"Usage: {sys.argv[0]} []")
    param = sys.argv[1]

def code_with_context_manager():
    with my_plain_context():
        print("  In plain context")
        if param == "return":
            return
        if param == "die":
            raise Exception("we have a problem")
        print("  More work")


@contextmanager
def my_plain_context():
    print("setup context")
    try:
        yield
    except Exception as err:
        print(f"  We got an exception: {err}")
    print("cleanup context")

print("START")
code_with_context_manager()
print("END")
