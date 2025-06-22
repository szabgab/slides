import subprocess
import time
import os
import psutil

def run_process(command):
    print(f"Before Popen {os.getpid()}")
    proc = subprocess.Popen(command)  # This starts runing the external process
    print(f"After Popen of {proc.pid}")
    psproc = psutil.Process(proc.pid)
    print(f"name: {psproc.name()}")
    print(f"cmdline: {psproc.cmdline()}")
    time.sleep(1.5)

    print("Before communicate")
    proc.communicate()
    print("After communicate")

    exit_code = proc.returncode
    return exit_code

print("Before run_process", flush=True)
exit_code = run_process(['python', 'process.py', '5', '0'])
print("After run_process", flush=True)

print(f'exit code: {exit_code}', flush=True)

