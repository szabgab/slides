import colors as cl

def main():
    print("start")
    try:
        cl.green()
    except Exception as err:
        print(err)
        print(type(err).__name__)
    print("done")


main()

