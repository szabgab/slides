import platform

def my_input(text):
    if platform.python_version_tuple()[0] == 3:
        return input(text)
    else:
        return raw_input(text)

