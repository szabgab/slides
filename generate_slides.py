#!/usr/bin/env python

import os
import sys
import shutil
import re
import argparse
import yaml
import json
import jinja2
import datetime

root   = os.path.dirname(os.path.abspath(__file__))
parent = os.path.dirname(root)
slider = "{}/slider-py/slider.py".format(parent)
#print("root={}".format(root))
#print("parent={}".format(parent))
if not os.path.exists(slider):
    exit("{} does not exist".format(slider))

def main():
    args = get_arguments()

    html_root = os.path.join(root, 'html')
    #print("html_root={}".format(html_root))
    if not args.keep:
        if os.path.exists(html_root):
            shutil.rmtree(html_root)
    if not os.path.exists(html_root):
        os.mkdir(html_root)

    if args.ext:
        ext = "--ext " + args.ext
    else:
        ext = ''

    names, books = select_books(args)
    if args.chapter:
        original_json_file = os.path.join(root, books[0]['dir'], books[0]['filename'])
        with open(original_json_file) as fh:
            data = json.load(fh)
        data['files'] = args.chapter
        temp_json_file = os.path.join(root, books[0]['dir'], 'temp.json')
        with open (temp_json_file, 'w') as fh:
            json.dump(data, fh, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)
        books[0]['filename'] = 'temp.json'

    #print(names)
    #print(books)


    generate_singles(names, ext)
    generate_multis(books, ext, args.hostname)
    generate_index(args.ext)
    generate_sitemap_xml(args.hostname)
    copy_static_files()

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ext', default='html')
    parser.add_argument('--keep', action='store_true')
    parser.add_argument('--chapter', nargs='+')
    parser.add_argument('--hostname', default='https://code-maven.com')
    parser.add_argument('names', nargs='*')
    args = parser.parse_args()

    return args


def select_books(args):
    available_names, available_books = get_availables()

    names = []
    books = []
    if len(args.names) > 0:
        for name in args.names:
            name = name.rstrip('/')
            name = name.replace('.json', '')
            if name in available_names:
                names.append(name)
                continue
            for book in available_books:
                if name == book['dir'] or name == book['outdir']:
                    books.append(book)
        if not names and not books:
            exit("Could not find any valid names or books")
    else:
        names = available_names
        books = available_books

    return names, books

def get_availables():
    available_names = []
    slides_path = os.path.join(root, 'slides.txt')
    if os.path.exists(slides_path):
        with open(slides_path) as fh:
            available_names = map(lambda s: s.rstrip("\n"), fh.readlines())

    with open(os.path.join(root, 'books.txt')) as fh:
        available_books = []
        for line in fh:
            line = line.rstrip("\n")
            if re.search(r'\A\s*(#.*)?\Z', line):
                continue
            #print(line)
            json_file, outdir, canonical = line.split(',')
            if not canonical:
                canonical = outdir
            bookdir, filename = json_file.split('/')
            available_books.append({
                'dir': bookdir,
                'filename': filename,
                'outdir': outdir,
                'canonical': canonical,
            })
    #print(available_books)
    return available_names, available_books


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

def generate_multis(books, ext, hostname):
    for book in books:
        print("{} - {} - {} - {}".format(book['dir'], book['filename'], book['outdir'], book['canonical']))
        cmd = '''{executable} "{slider}" --config "{root}/{bdir}/{bfilename}" --html --dir "{root}/html/{boutdir}/" --templates "{root}/templates/" --static "{root}/static/" --url "{hostname}/slides/{canonical}" {ext}'''.format(
            executable = sys.executable,
            hostname = hostname,
            slider = slider,
            root   = root,
            bdir   = book['dir'],
            bfilename = book['filename'],
            boutdir   = book['outdir'],
            canonical = book['canonical'],
            ext = ext,
        )
        #print("cmd={}".format(cmd))
        ret = os.system(cmd)
        if ret != 0:
            exit("Failed")

def generate_sitemap_xml(hostname):
    html_dir = os.path.join(root, 'html')
    ts = datetime.datetime.now().strftime("%Y-%m-%d")
    #print(ts)
    xml  = '''<?xml version="1.0" encoding="UTF-8"?>\n'''
    xml += '''<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'''
    xml += '''   <url>\n'''
    xml += f'''      <loc>{hostname}/slides/</loc>\n'''
    xml += '''      <lastmod>{ts}</lastmod>\n'''.format(ts=ts)
    xml += '''   </url>\n'''


    for subject in os.listdir(html_dir):
        if not os.path.isdir(os.path.join(html_dir, subject)):
            continue
        #print(subject)
        xml += '''   <url>\n'''
        xml += f'''      <loc>{hostname}/slides/{subject}</loc>\n'''
        xml += '''      <lastmod>{ts}</lastmod>\n'''.format(ts=ts)
        xml += '''   </url>\n'''

        for page in os.listdir(os.path.join(html_dir, subject)):
            if re.search(r'\.(js|css|yaml)\Z', page):
                continue
            if not os.path.isfile(os.path.join(html_dir, subject, page)):
                continue
            xml += '''   <url>\n'''
            xml += f'''      <loc>{hostname}/slides/{subject}/{page}</loc>\n'''
            xml += '''      <lastmod>{ts}</lastmod>\n'''.format(ts=ts)
            xml += '''   </url>\n'''
    xml += '''</urlset>\n'''

    with open(os.path.join(html_dir, 'sitemap.xml'), 'w') as fh:
        fh.write(xml)


def generate_index(ext):
    html_dir = os.path.join(root, 'html')
    templates_dir = os.path.join(root, 'templates')
    html_filename = os.path.join(html_dir, 'index')
    if ext:
        html_filename += '.' + ext

    courses = []
    for subject in os.listdir(html_dir):
        #print(subject)
        subdir = os.path.join(html_dir, subject)
        # skip files
        if not os.path.isdir(subdir):
            continue
        info_file = os.path.join(html_dir, subject, 'info.json')
        with open(info_file) as fh:
            info = json.load(fh)
            info['dir'] = subject
        courses.append(info)
    with open(os.path.join(html_dir, 'index.yaml'), 'w') as fh:
        fh.write(yaml.dump(courses, default_flow_style=False))
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(templates_dir))
    template = env.get_template('main.html')
    total = sum(map(lambda x: x['cnt'], courses))
    html = template.render(
        title='Code-Maven training courses',
        courses=sorted(courses, key=lambda x: x['cnt'], reverse=True),
        total=total,
        timestamp=datetime.datetime.now(),
    )
    with open(html_filename, 'w', encoding="utf-8") as fh:
        fh.write(html)

def copy_static_files():
    for entry in os.listdir(os.path.join(root, 'static')):
        shutil.copy(os.path.join(root, 'static', entry), os.path.join(root, 'html'))

    # we create an extra copy of the admin file because on the server we need it without the html
    html_dir = os.path.join(root, 'html')
    for subject in os.listdir(html_dir):
        subdir = os.path.join(html_dir, subject)
        if not os.path.isdir(subdir):
            continue
        shutil.copy(os.path.join(root, 'static', 'admin.html'), os.path.join(subdir, 'admin'))



main()


