from abc import abstractmethod, ABC

class IDoor(ABC):

    @abstractmethod
    def open(self):
        pass

class SolidDoor (IDoor):

    def __init__(self):
        pass

    def open(self):
        print("Opening door...")

d = SolidDoor()
d.open()
