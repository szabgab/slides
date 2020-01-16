import sys
import os
import json
import time
from mymodule import calc

def child(start, end):
    results = {}
    for ix in range(start, end):
        results[ix] = calc(ix)
    filename = str(os.getpid()) + '.json'
    with open(filename, 'w') as fh:
        json.dump(results, fh)
    exit()

def main(total_number, parallels):
    results = {}

    processes = []
    a_range = int(total_number / parallels)
    for cnt in range(parallels):
        start = 1 + cnt * a_range
        end =  start + a_range
        if cnt == parallels - 1:
            end = total_number + 1
        print(f"do: {start}-{end}")
        pid = os.fork()
        if pid:
            processes.append(pid) # parent
        else:
            child(start, end)
    for _ in range(len(processes)):
        pid, exit_code = os.wait()
        #print(pid, exit_code)
        filename = str(pid) + '.json'
        with open(filename) as fh:
            res = json.load(fh)
            print(f"{pid}: {res}")
            results.update(res)
        os.unlink(filename)
    return results

if __name__ == '__main__':
    if len(sys.argv) < 3:
        exit(f"Usage: {sys.argv[0]} NUMBER PARALLEL")

    start = time.time()
    results = main(int(sys.argv[1]), int(sys.argv[2]))
    print(f"results: {results}")
    end = time.time()
    total = sum(results.values())
    print(f"Total: {total}")
    print("Elapsed time: {}".format(end-start))



