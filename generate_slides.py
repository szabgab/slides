#!/usr/bin/env python

import os
import sys
import shutil
import re

# Possible arguments: (where NAME is one of the slides)
# --ext html
# NAME
# --ext html NAME

root   = os.path.dirname(os.path.abspath(__file__))
parent = os.path.dirname(root)
slider = f"{parent}/slider-py/slider.py"
#print(f"root={root}")
#print(f"parent={parent}")
if not os.path.exists(slider):
    exit(f"{slider} does not exist")

def main():
    html_root = os.path.join(root, 'html')

    #print(f"html_root={html_root}")
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
        available_names = map(lambda s: s.rstrip("\n"), fh.readlines())

    with open(os.path.join(root, 'books.txt')) as fh:
        available_books = []
        for line in fh:
            line = line.rstrip("\n")
            if re.search(r'\A\s*(#.*)?\Z', line):
                continue
            #print(line)
            bookdir, filename, outdir = re.split(r'[/,]', line)
            available_books.append({
                'dir': bookdir,
                'filename': filename,
                'outdir': outdir,
            })
    #print(available_books)

    names = []
    books = []
    if len(sys.argv) > 1:
        for name in sys.argv[1:]:
            if name in available_names:
                names.append(name)
                continue
            for book in available_books:
                if name == book['dir']:
                    books.append(book)
    else:
        names = available_names
        books = available_books
    #print(names)
    #print(books)

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
    for book in books:
        print(f"{book['dir']} - {book['filename']} - {book['outdir']}")
        cmd = f'''{sys.executable} "{slider}" --yaml "{root}/{book['dir']}/{book['filename']}" --html --dir "{root}/html/{book['outdir']}/" --templates "{root}/templates/" --static "{root}/static/" {ext}'''
        #print(f"cmd={cmd}")
        ret = os.system(cmd)
        if ret != 0:
            exit("Failed")


main()


