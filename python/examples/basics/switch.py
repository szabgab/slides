import sys

if len(sys.argv) != 2:
    print("Usage: python switch.py <status_code>")
    sys.exit(1)

status_code = int(sys.argv[1])

match status_code:
    case 401 | 302:
        print("401 or 302")
    case 200:
        print("200")
    case 200:
        print("200 again")
    case _:
        print("other")
