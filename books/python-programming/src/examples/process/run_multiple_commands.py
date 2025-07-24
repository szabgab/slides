import subprocess
import time
import os
import psutil

def run_process(*commands):
    print(f"Before Popen {os.getpid()}")
    processes = []
    for command in commands:
        proc = subprocess.Popen(command)  # This starts runing the external process
        print(f"After Popen of {proc.pid}")
        psproc = psutil.Process(proc.pid)
        print(f"name: {psproc.name()}")
        print(f"cmdline: {psproc.cmdline()}")
        processes.append(proc)

    time.sleep(1.5)

    print("Before communicate")
    for proc in processes:
        proc.communicate()
    print("After communicate")

    exit_codes = [proc.returncode for proc in processes]
    return exit_codes

print("Before run_process", flush=True)
exit_codes = run_process(
    ['python', 'process.py', '5', '0'],
    ['python', 'process.py', '4', '1'],
    ['python', 'process.py', '3', '2'],
    )
print("After run_process", flush=True)

print(f'exit code: {exit_codes}', flush=True)

