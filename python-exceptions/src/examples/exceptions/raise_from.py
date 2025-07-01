import sys

def lower():
    #print("starting lower")
    raise Exception("exception in lower")
    print("still here")

def upper(set_from):
    try:
        lower()
    except Exception as err:
        if set_from == "Default":
            raise Exception("from upper")
        elif set_from == "None":
            raise Exception("from upper") from None
        elif set_from == "Same":
            raise Exception("from upper") from err
        else:                      
            raise Exception("from upper") from Exception("Incorrect input")


def main():
    if len(sys.argv) != 2:
        exit("Usage: raise_from.py [Default|None|Same]")

    param = sys.argv[1]

    # try:
    #     upper(param)
    # except Exception as err:
    #     print("err:", err)
    #     print("cause:", err.__cause__)
    #     print("context:", err.__context__)

    upper(param)

main()