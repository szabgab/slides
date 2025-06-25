import subprocess

def get_python_version():
    proc = subprocess.Popen(['python', '-V'],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
    )

    out,err = proc.communicate()
    if proc.returncode:
        raise Exception(f"Error exit {proc.returncode}")
    #if err:
    #    raise Exception(f"Error {err}")
    if out:
        return out.decode('utf8') # In Python 3.8.6
    else:
        return err.decode('utf8') # In Python 2.7.18
