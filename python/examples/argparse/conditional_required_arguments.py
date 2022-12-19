import argparse
import sys

# Python Argparse conditionally required arguments

print(sys.argv)
main_parser = argparse.ArgumentParser(add_help=False)
main_parser.add_argument('--commit',    help='Commit the downloaded data to git', action='store_true')
main_parser.add_argument('--html',      help='Generate the HTML report', action='store_true')
main_parser.add_argument('--collect',   help='Get the data from the Forem API', action='store_true')
main_args, _ = main_parser.parse_known_args()

#print(main_args)
print(main_args.commit)
print(main_args.html)
print(main_args.collect)
print(sys.argv)

parser = argparse.ArgumentParser(parents=[main_parser])
if main_args.collect:
    parser.add_argument('--username',  help='The username on the Forem site', required=main_args.collect)
    parser.add_argument('--host',      help='The hostname of the Forem site', required=main_args.collect)
    parser.add_argument('--limit',     help='Max number of pages to fetch', type=int)

args = parser.parse_args()



print(args.collect)
if args.collect:
    print(args.username)
    print(args.host)
    print(args.limit)

print(args.html)
print(args.commit)

