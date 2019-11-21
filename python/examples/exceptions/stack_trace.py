import traceback

def bar():
    foo()

def foo():
    raise Exception("hi")

def main():
    try:
        bar()
    except Exception as err:
        track = traceback.format_exc()
        print(track)

    print("---------------------")
    bar()


main()
