import subprocess
import time

def run_process(command):
    print("Before Popen")
    proc = subprocess.Popen(command,
        stdout = subprocess.PIPE,
        stderr = subprocess.STDOUT,
    )  # This starts runing the external process
    print("After Popen")
    time.sleep(1.5)

    print("Before communicate")
    out, err = proc.communicate()
    print("After communicate")

    # out and err are two strings
    exit_code = proc.returncode
    return exit_code, out, err

print("Before run_process")
exit_code, out, err = run_process(['python', 'process.py', '5', '0'])
print("After run_process")

print("")
print(f'exit code: {exit_code}')

print("")
print('out:')
for line in out.decode('utf8').split('\n'):
    print(line)

print('err:')
print(err)
