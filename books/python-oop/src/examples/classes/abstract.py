import abc

class Port():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def num(self):
        pass

class HTTPPort(Port):
    def num(self):
        return 80

class FTPPort(Port):
    def num(self):
        return 21

class ZorgPort(Port):
    def nonum(self):
        return 'zorg'

f = FTPPort()
print(f.num())
h = HTTPPort()
print(h.num())
z = ZorgPort()
# Traceback (most recent call last):
#   File "abstract.py", line 26, in <module>
#     z = ZorgPort()
# TypeError: Can't instantiate abstract class ZorgPort with abstract methods num


print(z.num())

