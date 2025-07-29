import os

for ix in range(10):
    filename = f'data{ix}.txt'
    fh = open(filename, 'w')
    fh.write('hello')
    if ix == 0:
        break
    fh.close()
stat = os.stat(filename)
print(stat.st_size)    # 0,   the file has not been saved yet
