import subprocess
import sys
import time

def run_process(command, timeout):
    print("Before Popen")
    proc = subprocess.Popen(command,
       stdout = subprocess.PIPE,
       stderr = subprocess.PIPE,
    )
    print("After Popen")

    while True:
       poll = proc.poll()
       print(f"poll: {poll}")
       time.sleep(0.5)  # here we could actually do something useful
       timeout -= 0.5
       if timeout <= 0:
           break
       if poll is not None:
           break

    print(f"Final: {poll}")
    if poll is None:
        raise Exception("Timeout")

    exit_code = proc.returncode
    out, err = proc.communicate()
    return exit_code, out, err

exit_code, out, err = run_process([sys.executable, 'process.py', '3', '0'], 6)

print("-----")
print(f"exit_code: {exit_code}")
print("OUT")
print(out.decode())
print("ERR")
print(err.decode())

