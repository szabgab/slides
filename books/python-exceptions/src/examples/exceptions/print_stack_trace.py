import traceback

def foo():
  bar()

def bar():
    #print(traceback.extract_stack())
    print(''.join(traceback.format_stack()))

foo()
print("done")

#   File "python/examples/other/print_stack_trace.py", line 10, in <module>
#     foo()
#   File "python/examples/other/print_stack_trace.py", line 4, in foo
#     bar()
#   File "python/examples/other/print_stack_trace.py", line 8, in bar
#     print(''.join(traceback.format_stack()))
#
# done

