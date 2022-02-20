import cv2 as cv
import sys
import os

WAIT_TIME = 100
START_HEIGHT = 300
MAX_HEIGHT = 600

def resize(img, current_height):
    print(img.shape)
    height, width, colors = img.shape

    if height > current_height:
        scale = current_height/height
        new_height = int(height * scale)
        new_width = int(width * scale)
        img = cv.resize(img, (new_width, new_height), interpolation=cv.INTER_AREA)
    return img

def slider_changed(event):
    pass
    #print('slider')
    #print(event)

def get_size():
    slider = cv.getWindowProperty('slider', cv.WND_PROP_VISIBLE)
    #print(slider)
    current_height = START_HEIGHT
    if slider > 0:
        current_height = cv.getTrackbarPos("Size", "slider")
    #print(current_height)
    return current_height


def main():
    if len(sys.argv) != 2:
        exit(f"Usage: {sys.argv[0]} DIRNAME")


    dirname = sys.argv[1]
    files = list(filter(lambda thing: not os.path.isdir(thing), map(lambda filename: os.path.join(dirname, filename), os.listdir(dirname))))
    #print(files)
    prev_idx = -1
    prev_height = 0
    idx = 0

    cv.namedWindow("slider")
    ##cv.resizeWindow("slider", 640, 45)
    cv.createTrackbar("Size", "slider", START_HEIGHT, MAX_HEIGHT, slider_changed)

    while True:
        current_height = get_size()
        if idx != prev_idx or current_height != prev_height:
            prev_idx = idx
            prev_height = current_height
            filename = files[idx]
            img = cv.imread(filename)

            img = resize(img, current_height)
            cv.imshow('img', img)

        # Make sure application exits if we close the window of the image
        visible = cv.getWindowProperty('img', cv.WND_PROP_VISIBLE)
        if visible == 0.0:
            cv.destroyAllWindows()
            break

        key = cv.waitKey(WAIT_TIME)
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
