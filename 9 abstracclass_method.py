from abc import *

'''
import abc

abc.ABC()
abc.abstractmethod()
abc.abstractclassmethod()
abc.abstractstaticmethod()
abc.abstractproperty()

@abc.abstractproperty.getter
@abc.abstractproperty.setter
@abc.abstractproperty.deleter
'''

class Animal(ABC):

    @abstractmethod
    def __init__(self, name):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, name):
        pass

    @name.deleter
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def giveVoice(self):
        pass

class Cat(Animal):

    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @name.deleter
    def name(self):
        self.__name = None

    def giveVoice(self):
        print("Miau!")


cat = Cat("miałek")
cat.giveVoice()