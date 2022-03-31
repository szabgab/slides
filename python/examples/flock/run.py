import subprocess
import sys

if len(sys.argv) != 4:
    exit(f"Usage: {sys.argv[0]} FILENAME count processes")
filename, count, process_count = sys.argv[1:]

command = [sys.executable, 'count.py', filename, count]
processes = []
for _ in range(int(process_count)):
    processes.append(subprocess.Popen(command))
print('Started')
for proc in processes:
    proc.communicate()
print('Done')
