import argparse
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name')
    parser.add_argument('--email')

    print(dir(parser))
    print( parser.format_help() )
    parser.print_help()

    return parser.parse_args()

args = get_args()

