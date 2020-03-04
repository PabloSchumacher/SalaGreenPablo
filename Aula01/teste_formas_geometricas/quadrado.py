class Quadrado:
    def __init__(self, lateral):
        self.__lateral = lateral

    def set_lado(self, __lateral):
        self.__lateral = __lateral

    def get_lado(self, __lateral):
        return self.__lateral

    def calcular_area(self, __lateral):
        return __lateral * __lateral