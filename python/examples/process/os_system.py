import os
import sys

exit_code = os.system(f"{sys.executable} process.py 5 0")
print(f'exit code: {exit_code}')

