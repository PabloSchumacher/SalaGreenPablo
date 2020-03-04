from Calculadora.Operacoes import Opecacoes

class Perguntas:

    def __init__(self, n1,n2,tipo):
        self.__n1 = n1
        self.__n2 = n2
        self.__tipo = tipo

    def set_n1(self, n1):
        a = 1
        while a == 1:
            try:
                self.__n1 = float(input('Informe o primeiro número: '))
                a = 2
            except ValueError:
                print('Você deve digitar apenas valores numéricos.')
        return self.__n1

    def set_n2(self, n2):
        a = 1
        while a == 1:
            try:
                self.__n2 = float(input('Informe o segundo número: '))
                a = 2
            except ValueError:
                print('Você deve digitar apenas valores numéricos.')
        return self.__n2

    def set_tipo(self,tipo):
        self.__tipo = 0
        while self.__tipo <=0 or self.__tipo >6:
            try:
                self.__tipo = int(input('''Informe o tipo de operação que deseja:
                1- Soma
                2- Subtração
                3- Multiplicação
                4- Divisão decimal
                5- Divisão exata
                6- Resto da divisão
    
                Resposta: '''))
            except ValueError:
                print('Você deve digitar um dos números correspontes as operações acima, apenas valores numéricos.')
        return self.__tipo

    def get_resposta(self,n1,n2,tipo):
        Calc = Opecacoes()
        if self.__tipo == 1:
            return (Calc.soma(n1, n2))
        elif self.__tipo == 2:
            return (Calc.subtracao(n1, n2))
        elif self.__tipo == 3:
            return (Calc.multiplicacao(n1, n2))
        elif self.__tipo == 4:
            return (Calc.divisao_decimal(n1, n2))
        elif self.__tipo == 5:
            return (Calc.divisao_exata(n1, n2))
        elif self.__tipo == 6:
            return (Calc.resto(n1, n2))

calc = Perguntas(0,0,0)
n1 = calc.set_n1(0)
tipo = calc.set_tipo(0)
n2 = calc.set_n2(0)
print(calc.get_resposta(n1,n2,tipo))