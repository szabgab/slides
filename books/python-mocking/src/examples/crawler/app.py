import sys
import requests
import re

def count(url, word):
    r = requests.get(url)
    # r.status_code
    res = re.findall(word, r.text, re.IGNORECASE)
    return(len(res))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        exit("{} URL string".format(sys.argv[0]))
    print(count(sys.argv[1], sys.argv[2]))
