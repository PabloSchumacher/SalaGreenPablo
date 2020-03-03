from Operacoes import Opecacoes

class Perguntas:
    def pergunta_numero():
        a = 1
        while a == 1:
            try:
                n1 = float(input('Digite o primeiro número: '))
                n2 = float(input('Digite o segundo número: '))
                a = 2
            except ValueError:
                print('Você é um macaco que digitou errado, faz de novo.')

    def pergunta_tipo():
        resposta = 0
        while resposta == 0:
            try:
                resposta = int(input('''Qual tipo de operação você deseja fazer?:
                1- Soma
                2- Subtração
                3- Multiplicação
                4- Divisão decimal
                5- Divisão exata
                6- Resto da divisão
    
                Resposta: '''))
            except ValueError:
                print('Você é um macaco que digitou errado, faz de novo.')
        return resposta

    def resposta(b):
        Calc = Opecacoes()
        if resposta == 1:
            return (Calc.soma(n1, n2))
        elif resposta == 2:
            return (Calc.subtracao(n1, n2))
        elif resposta == 3:
            return (Calc.multiplicacao(n1, n2))
        elif resposta == 4:
            return (Calc.divisao_decimal(n1, n2))
        elif resposta == 5:
            return (Calc.divisao_exata(n1, n2))
        elif resposta == 6:
            return (Calc.resto(n1, n2))
