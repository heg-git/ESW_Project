from abc import *
class ObjectPool(metaclass=ABCMeta):
    @abstractmethod
    def create_object(self):
        pass

    @abstractmethod
    def take_object(self):
        pass

    @abstractmethod
    def put_object(self):
        pass
    
