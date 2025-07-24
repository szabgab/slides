import subprocess
import sys
import time

def run_process(command, timeout):
    print("Before Popen")
    proc = subprocess.Popen(command,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        universal_newlines=True,
        bufsize=0,
    )
    print("After Popen")
    out = ""
    err = ""

    while True:
        exit_code = proc.poll()
        print(f"poll: {exit_code} {time.time()}")
        this_out = proc.stdout.readline()
        this_err = proc.stderr.readline()
        print(f"out: {this_out}", end="")
        print(f"err: {this_err}", end="")
        out += this_out
        err += this_err
        time.sleep(0.5)  # here we could actually do something useful
        timeout -= 0.5
        if timeout <= 0:
            break
        if exit_code is not None:
            break

    print(f"Final: {exit_code}")
    if exit_code is None:
        raise Exception("Timeout")

    return exit_code, out, err

exit_code, out, err = run_process([sys.executable, 'process.py', '4', '3'], 20)
#exit_code, out, err = run_process(['docker-compose', 'up', '-d'], 20)

print("-----")
print(f"exit_code: {exit_code}")
print("OUT")
print(out)
print("ERR")
print(err)

