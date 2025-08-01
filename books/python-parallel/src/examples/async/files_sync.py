import tempfile
import os


def save_file(filename, size):
    with open(filename, 'w') as f:
        for _ in range(size):
            data = ''
            for _ in range(1000):
                data += 'xxxxxxxxxxx'

            f.write(data)

def main():
    tempdir = tempfile.mkdtemp()
    for idx in range(300):
        filename = os.path.join(tempdir, f'{idx}.txt')
        save_file(filename, 100)

main()
