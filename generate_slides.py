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
slider = "{}/slider-py/slider.py".format(parent)
#print("root={}".format(root))
#print("parent={}".format(parent))
if not os.path.exists(slider):
    exit("{} does not exist".format(slider))

def main():
    html_root = os.path.join(root, 'html')

    #print("html_root={}".format(html_root))
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
        cmd = '{executable} "{slider}" --md "{root}/{name}/intro.md" --html --dir "{root}/html/{name}/" --templates "{root}/templates/" --static "{root}/static/" {ext}'.format(
            executable = sys.executable,
            slider = slider,
            root = root,
            name = name,
            ext  = ext,
        )
        #print("cmd={}".format(cmd))
        ret = os.system(cmd)
        if ret != 0:
            exit("Failed")

def generate_multis(books, ext):
    for book in books:
        print("{} - {} - {}".format(book['dir'], book['filename'], book['outdir']))
        cmd = '''{executable} "{slider}" --yaml "{root}/{bdir}/{bfilename}" --html --dir "{root}/html/{boutdir}/" --templates "{root}/templates/" --static "{root}/static/" {ext}'''.format(
            executable = sys.executable,
            slider = slider,
            root   = root,
            bdir   = book['dir'],
            bfilename = book['filename'],
            boutdir   = book['outdir'],
            ext = ext,
        )
        #print("cmd={}".format(cmd))
        ret = os.system(cmd)
        if ret != 0:
            exit("Failed")


main()


