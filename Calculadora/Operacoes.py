class Opecacoes:
    def __init__(self,n1,n2):
        self.__n1 = n1
        self.__n2 = n2

    def soma(self, n1,n2):
        return self.__n1+self.__n2

    def subtracao(self,n1,n2):
        return self.__n1-self.__n2

    def multiplicacao(self,n1,n2):
        return self.__n1*self.__n2

    def divisao_decimal(self,n1,n2):
        return self.__n1/self.__n2

    def divisao_exata(self,n1,n2):
        return self.__n1//self.__n2

    def resto(self,n1,n2):
        return self.__n1%self.__n2