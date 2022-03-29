import subprocess
import sys

def run_process(command):
    print("Before Popen")
    proc = subprocess.Popen(command,
    )  # This starts runing the external process
    print("After Popen")

    proc.communicate()
    print("After communicate")

    exit_code = proc.returncode
    return exit_code

print("Before run_process")
exit_code = run_process([sys.executable, 'process.py', '5', '0'])
print("After run_process")

print(f'exit code: {exit_code}')

