main()
    ...
    try:
        ...
        result = do_something(filename)
        do_something_else(result)
    except Exception:
        decide_what_to_do()

    always_happens()
