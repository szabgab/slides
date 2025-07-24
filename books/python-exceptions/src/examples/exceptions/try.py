
def divide(x, y):
    return x/y

def main():
    cnt = 6
    for num in [2, 0, 'a']:
        try:
            divide(cnt, num)
        except ZeroDivisionError:
            pass
        except (IOError, MemoryError) as err:
            print(err)
        else:
            print("This will run if there was no exception at all")
        finally:
            print("Always executes. {}/{} ended.".format(cnt, num))

    print("done")


main()

