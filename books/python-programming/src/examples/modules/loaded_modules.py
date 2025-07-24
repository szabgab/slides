for mod in sorted(sys.modules.keys()):
    try:
        print(mod, sys.modules[mod].__file__)
    except Exception as err:
        print(mod)
