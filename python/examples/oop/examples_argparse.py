import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name')
    parser.add_argument('--email')

    print(type(parser).__name__) # ArgumentParser
    print(parser.__class__)      # <class 'argparse.ArgumentParser'>

    # print(dir(parser))
    # print( parser.format_help() )
    # parser.print_help()

    return parser.parse_args()

args = get_args()
print(args.__class__) # <class 'argparse.Namespace'>
print(args.name)      # None
