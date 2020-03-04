import math

class Circulo:
    def __init__(self, cor, raio, material):
        self.__cor = cor
        self.__raio = raio
        self.__material = material

    def set_cor(self,cor):
        self.__cor = cor

    def get_cor(self,cor):
        return self.__cor

    def calcular_area(self,raio):
        return math.pi*raio**2
