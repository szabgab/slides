import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name')

action = parser.add_mutually_exclusive_group(required=True)
action.add_argument('--add', action='store_true')
action.add_argument('--remove', action='store_true')

args = parser.parse_args()
