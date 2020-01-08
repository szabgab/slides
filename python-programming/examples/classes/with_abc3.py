from abc import ABC, abstractmethod

class Base(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass

