class Pracownik:

    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @name.deleter
    def name(self):
        print("Deleted")
        self.__name = None


p1 = Pracownik("Bartosz", "Twardy")
p1.name = "Tomasz"
print(p1.name)
del p1.name