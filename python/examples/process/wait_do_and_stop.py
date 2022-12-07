#import os
#import time
#import signal
import subprocess
import sys
import time


#def test_hello():
#    run_process([sys.executable, "examples/Hello-World.py"], )
    #pid = os.fork()
    #if pid is None:
    #    raise Exception("Could not fork")

    #if pid:
    #    print(f"parent of {pid}")
    #    time.sleep(5)
    #    os.kill(pid, signal.SIGKILL)
    #else:
    #    print("child")
    #    os.environ['PYTHONPATH'] = '.'
    #    os.exec("python examples/Hello-World.py")


def run_process(command, start_timeout):
    sleep_time = 0.5
    print(command)
    proc = subprocess.Popen(command,
        stdout = subprocess.PIPE,
        stderr = subprocess.STDOUT,
        universal_newlines=True,
        bufsize=0,
    )

    out = ""
    while True:
        print("Loop")
        exit_code = proc.poll()  # returns the exit code or None if the process is still running
        if exit_code is not None:
            raise Exception("Server died")
        print(exit_code)
        this_out = proc.stdout.readline()
        #this_err = proc.stderr.readline()
        out += this_out
        print(f"Before sleep {sleep_time} for a total of {start_timeout}")
        time.sleep(sleep_time)
        start_timeout -= sleep_time
        if start_timeout <= 0:
            proc.terminate()
            raise Exception("The service has not properly started")

        if "started" in out:
            print(out)
            print("--------")
            print("It is now running")
            print("--------")
            break

    print("Do something interesting here that takes 2 seconds")
    time.sleep(2)
    proc.terminate()

    exit_code = proc.returncode
    out, _ = proc.communicate()
    return exit_code, out

print("Before")
exit_code, out = run_process([sys.executable, 'slow_starting_server.py', '3'], 4)
print("-----")
print(f"exit_code: {exit_code}")
print("OUT")
print(out)

