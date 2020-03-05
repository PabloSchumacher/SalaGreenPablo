class Retangulo:
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    def set_base(self, base):
        self.__base = base

    def set_altura(self, altura):
        self.__altura = altura

    def get_base(self):
        return self.__base

    def get_altura(self):
        return self.__altura

    def calcular_area(self, base, altura):
        return self.__base*self.__altura
