import subprocess

def capture(command):
    proc = subprocess.Popen(command,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
    )
    out,err = proc.communicate()
    return out, err, proc.returncode


def test_anagram_no_param():
    command = ["python3", "examples/pytest/anagram.py"]
    out, err, exitcode = capture(command)
    assert exitcode == 1
    assert out == b''
    assert err == b'Usage examples/pytest/anagram.py STR STR\n'

def test_anagram():
    command = ["python3", "examples/pytest/anagram.py", "abc", "cba"]
    out, err, exitcode = capture(command)
    assert exitcode == 0
    assert out == b'True\n'
    assert err == b''

def test_no_anagram():
    command = ["python3", "examples/pytest/anagram.py", "abc", "def"]
    out, err, exitcode = capture(command)
    assert exitcode == 0
    assert out == b'False\n'
    assert err == b''

