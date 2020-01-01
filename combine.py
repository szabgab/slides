#!/usr/bin/env python

import argparse
import logging
import os
import shutil
import time

# TODO: git clean -dXf

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', help='name of the slides')
    parser.add_argument('--all', action='store_true', help='collect all the slides')
    parser.add_argument('--target', help='Optional target directory. If not given automatically set.')
    return parser.parse_args()

def process_slides(source, target, name):
    logging.info(f"Processing slides of {name}")
    book = []

    resources = os.path.join(target, 'resources')
    if not os.path.exists(resources):
        os.mkdir(resources)

    slides_path = os.path.join(source, name)
    for thing in os.listdir(slides_path):
        if thing in ['examples', 'README.md', 'img', 'Dockerfile', '.idea', 'python.json']:
            continue
        thing_path = os.path.join(slides_path, thing)
        if os.path.isfile(thing_path) and thing.endswith('.md'):
            new_filename = f"{name}-{thing}"
            shutil.copy(thing_path, os.path.join(target, new_filename))
            book.append(new_filename)
        else:
            exit(f"What is this thing {thing_path} ?")
            logging.warning(f"What is this thing {thing_path} ?")

    src_examples = os.path.join(slides_path, 'examples')
    if os.path.exists(src_examples):
        for example in os.listdir(src_examples):
            #print(example)
            example_path = os.path.join(src_examples, example)
            if os.path.islink(example_path):
                logging.debug(f"Skipping symlink {example_path}")
            elif os.path.isdir(example_path):
                logging.debug(f"Copy dir {example_path}")
                shutil.copytree(example_path, os.path.join(resources, 'examples', example))
            else:
                exit(f"Could not handle: {example_path}")
                #logging.error(f"{example_path}")
                # TODO maybe I should not even handle this just let the code blow up so I will be forced to fix
                # this

    src_img = os.path.join(slides_path, 'img')
    img_dir = os.path.join(resources, 'img')
    if not os.path.exists(img_dir):
        os.mkdir(img_dir)
    if os.path.exists(src_img):
        for img in os.listdir(src_img):
            img_path = os.path.join(src_img, img)
            if os.path.isfile(img_path):
                logging.debug(f"Copy image: {img_path}")
                shutil.copy(img_path, os.path.join(resources, 'img', img))


    return book


def main():
    logging.basicConfig(
        level = logging.DEBUG,
        format = '%(asctime)s - %(levelname)-5s - %(funcName)s - %(name)s - %(message)s',
        datefmt = "%Y-%m-%d %H:%M:%S"
    )
    args = get_arguments()

    root = os.path.dirname(os.path.abspath(__file__))
    start = time.time()

    if args.all:
        target = os.path.join(root, '../slides-all-book-generated')
    elif args.name:
        target = os.path.join(root, f'../slides-{args.name}-book-generated')
    else:
        exit("Either --all or --name must be provided")

    if args.target:
        target = args.target

    target = os.path.abspath(target)
    target = os.path.join(target, 'manuscript')

    source = os.path.abspath(root)
    logging.info(f"target: {target}")
    logging.info(f"source: {source}")

    if os.path.exists(target):
        shutil.rmtree(target)
    os.mkdir(target)

    book = []
    if args.all:
        slides_file = os.path.join(source, 'slides.txt')
        with open(slides_file, 'r') as fh:
            for line in fh:
                line = line.rstrip("\n")
                book.extend(process_slides(source, target, line))
        # extra directories that are not in the list of slides yet
        for line in ['python']:
            book.extend(process_slides(source, target, line))
    else:
        book = process_slides(source, target, args.name)

    with open(os.path.join(target, 'Book.txt'), 'w') as fh:
        for line in book:
            fh.write(line + "\n")
    end = time.time()
    logging.info("Done. Elapsed time: {}".format(end-start))


main()


