import inspect

def first():
    second()


def second():
    for info in inspect.stack():
        #print(info)
        #FrameInfo(
        #    frame=<frame at 0x1c18b18, file 'stack_trace.py', line 9, code second>,
        #    filename='stack_trace.py',
        #    lineno=8,
        #    function='second',
        #    code_context=['    for level in inspect.stack():\n'],
        #    index=0)

        #print(info.frame)
        print(info.filename)
        print(info.lineno)
        print(info.function)
        print(info.code_context)
        print('')

def main():
    first()


if __name__ == '__main__':
    main()

