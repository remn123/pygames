
from concepts import Creatable

class IFactory(object):
    
    @staticmethod
    def make(self, type_: str,  params: dict):
        pass
            

class Factory(IFactory):

    @staticmethod
    def make(type_: str, params: dict):
        list_of_types = [cls.__name__.lower() for cls in Creatable.__subclasses__()]
        if type_ in list_of_types:
            print(f"Creating object of type: {type_}")
            return [cls(**params) for cls in Creatable.__subclasses__() if cls.__name__.lower() == type_][0]
        else:
            raise TypeError(f"Type {type_} is not an implemented subclass of Creatable.\nPossibles are: {list_of_types}.")
