#!/usr/bin/env python

import os
import sys
import shutil

# Possible arguments: (where NAME is one of the slides)
# --ext html
# NAME
# --ext html NAME

root   = os.path.dirname(os.path.abspath(__file__))
parent = os.path.dirname(root)
slider = f"{parent}/slider-py/slider.py"
print(f"root={root}")
print(f"parent={parent}")
if not os.path.exists(slider):
    exit(f"{slider} does not exist")

def main():
    html_root = os.path.join(root, 'html')

    print(f"html_root={html_root}")
    if os.path.exists(html_root):
        shutil.rmtree(html_root)
    os.mkdir(html_root)

    # ext=""
    # if [ "$1" == "--ext" ]
    # then
    #     ext="--ext $2"
    #     shift
    #     shift
    # fi
    ext = "--ext html"
    with open(os.path.join(root, 'slides.txt')) as fh:
        names = map(lambda s: s.rstrip("\n"), fh.readlines())

    with open(os.path.join(root, 'books.txt')) as fh:
        books = dict(map(lambda x: x.split('/'), map(lambda s: s.rstrip("\n"), fh.readlines())))


    if len(sys.argv) == 2:
        only_one = sys.argv[1]
        if only_one in names:
            names = [only_name]
            books = {}
        elif only_name in books:
            names = []
            books = { only_name :  books[only_name] }

    generate_singles(names, ext)
    generate_multis(books, ext)

def generate_singles(names, ext):
    for name in names:
        print(name)
        cmd = f'{sys.executable} "{slider}" --md "{root}/{name}/intro.md" --html --dir "{root}/html/{name}/" --templates "{root}/templates/" --static "{root}/static/" {ext}'
        #print(f"cmd={cmd}")
        ret = os.system(cmd)
        if ret != 0:
            exit("Failed")

def generate_multis(books, ext):
    for (name, filename) in books.items():
        print(f"{name} - {filename}")
        cmd = f'{sys.executable} "{slider}" --yaml "{root}/{name}/{filename}" --html --dir "{root}/html/{name}/" --templates "{root}/templates/" --static "{root}/static/" {ext}'
        #print(f"cmd={cmd}")
        ret = os.system(cmd)
        if ret != 0:
            exit("Failed")


main()


