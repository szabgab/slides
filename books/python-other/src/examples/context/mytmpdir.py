import os
from contextlib import contextmanager
import tempfile
import shutil

@contextmanager
def tmpdir():
    dd = tempfile.mkdtemp()
    try:
        yield dd
    finally:
        shutil.rmtree(dd)
