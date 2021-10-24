from observer import Subscriber
from module_a import ClassA

class ClassB(Subscriber):
    def __init__(self, name="Class B"):
        Subscriber.__init__(self, name)

    def register(self):
        self.update()
