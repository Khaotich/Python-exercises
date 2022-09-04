class Pracownik:
    __placa = 1500

    def __init__(self, name, subname):
        self.name = name
        self.surname = subname
        self.__llaca = Pracownik.__placa

    def getFullName(self):
        return self.name + " " + self.surname

    def getPlaca(self):
        return self.__llaca

    @classmethod
    def setPlaca(cls, p):
        cls.__placa = p

    @staticmethod
    def cos(string: str):
        print(string)

p1 = Pracownik("Bartosz", "Twardy")
print(p1.getPlaca())
Pracownik.setPlaca(2300)
p2 = Pracownik("Bartosz", "Mazurek")
print(p1.getPlaca())
Pracownik.cos("siema")