import os
import glob

files = glob.glob("*.py")
# print(files)
count = len(files)
print(f"Number of items to process: {count}")

parallel = 4   # How many in parallel

batch = int(count/parallel)
leftover = count % parallel
print(f"batch size: {batch}  leftover: {leftover}")

def parent(pid):
    print(f"parent {pid}")

def child(files):
    print(f"{os.getpid()}  {files}")
    exit()

end = 0
for ix in range(parallel):
    start = end
    end   = start + batch
    if ix < leftover:
        end += 1
    print(f"start={start} end={end}")

    pid = os.fork()
    if pid:
        parent(pid)
    else:
        child(files[start:end])

print(f"In parent {os.getpid()}")
for ix in range(parallel):
    r = os.wait()
    print(r)
