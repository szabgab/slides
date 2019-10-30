
def divide(x, y):
    try:
        print(x/y)
    except ZeroDivisionError:
        pass 
    except (IOError, MemoryError) as e:
        pass
    else:
        print("This will run if there was no exception at all")
    finally:
        print("Always executes. {}/{} ended.".format(x, y))


divide(6, 2)
divide(6, 0)
divide(6, "a")
print("ater all")

