class MyError(Exception):
    pass

class MyGreenError(MyError):
    pass

class MyBlueError(MyError):
    pass


def green():
    raise MyGreenError('Hulk')

def blue():
    raise MyBlueError('Frozen')

def red():
     red_alert()

