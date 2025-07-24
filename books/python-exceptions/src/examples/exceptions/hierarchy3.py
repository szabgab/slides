import colors as cl

def main():
    print("start")

    try:
        cl.green()
    except cl.MyError as err:
        print(err)
        print(type(err).__name__)

    try:
        cl.blue()
    except cl.MyError as err:
        print(err)
        print(type(err).__name__)

    try:
        cl.red()
    except cl.MyError as err:
        print(err)
        print(type(err).__name__)




    print("done")


main()

