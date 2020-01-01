def external_func():
    the_answer = 42 

    def func(args):
        print args, "the_answer:", the_answer

        # the_answer = 'what was the question?'
        # enabling this would give:
        # UnboundLocalError: local variable 'the_answer'
        #      referenced before assignment

    func("first")
    func("second")

external_func()

