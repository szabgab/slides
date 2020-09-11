#!/usr/bin/python3

import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('url',                      help='The url to fetch')
parser.add_argument('-I',  action='store_true', help='Show headers only')
args = parser.parse_args()

res = requests.get(args.url)
if args.I:
    for k in res.headers.keys():
        print(f"{k} = {res.headers[k]}")
    exit()

print(res.text)

