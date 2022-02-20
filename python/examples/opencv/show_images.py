import cv2 as cv
import sys
import os

MAX_HEIGHT = 300

def resize(img):
    print(img.shape)
    height, width, colors = img.shape
    if height > MAX_HEIGHT:
        scale = MAX_HEIGHT/height
        new_height = int(height * scale)
        new_width = int(width * scale)
        img = cv.resize(img, (new_width, new_height), interpolation=cv.INTER_AREA)
    return img


def main():
    if len(sys.argv) != 2:
        exit(f"Usage: {sys.argv[0]} DIRNAME")


    dirname = sys.argv[1]
    files = list(filter(lambda thing: not os.path.isdir(thing), map(lambda filename: os.path.join(dirname, filename), os.listdir(dirname))))
    #print(files)
    prev_idx = -1
    idx = 0

    while True:
        if idx != prev_idx:
            prev_idx = idx
            filename = files[idx]
            img = cv.imread(filename)
            img = resize(img)
            cv.imshow('img', img)

        key = cv.waitKey(100)
        if key == -1:
            continue
        print(f'key {key} pressed')
        if key == ord('q') or key == ord('x'):
            cv.destroyAllWindows()
            break
        if key == ord('n'):
            idx += 1
        if key == ord('p'):
            idx -= 1
        idx = idx % len(files)


main()
print('after main')
