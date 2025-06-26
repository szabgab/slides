import argparse

def get_args():
    print(type(argparse))            # <class 'module'>

    parser = argparse.ArgumentParser()
    print(parser.__class__)          # <class 'argparse.ArgumentParser'>
    print(parser.__class__.__name__) # ArgumentParser

    parser.add_argument('--name')
    parser.add_argument('--email')

    # print(dir(parser))
    # print( parser.format_help() )
    # parser.print_help()

    return parser.parse_args()

args = get_args()
print(args.__class__)          # <class 'argparse.Namespace'>
print(args.__class__.__name__) # Namespace

print(args.name)      # None
