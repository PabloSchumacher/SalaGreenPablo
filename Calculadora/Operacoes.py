class Opecacoes:
    def soma(self, n1,n2):
        resposta = n1+n2
        return f'{n1}+{n2} = {resposta}'

    def subtracao(self,n1,n2):
        resposta = n1-n2
        return f'{n1}-{n2} = {resposta}'

    def multiplicacao(self,n1,n2):
        resposta = n1*n2
        return f'{n1}*{n2} = {resposta}'

    def divisao_decimal(self,n1,n2):
        resposta = n1/n2
        return f'{n1}/{n2} = {resposta}'

    def divisao_exata(self,n1,n2):
        resposta = n1//n2
        return f'{n1}//{n2} = {resposta}'

    def resto(self,n1,n2):
        resposta = n1%n2
        return f'O da divisão entre {n1} e {n2} é: {resposta}'