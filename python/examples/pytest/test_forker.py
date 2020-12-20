import os
import pytest

def test_forker():
    pid = os.fork()
    if not pid:
        print("child")
    else:
        print(f"parent of {pid}")

