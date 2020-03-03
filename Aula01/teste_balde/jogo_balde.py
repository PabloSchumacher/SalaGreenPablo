from Aula01.teste_balde.balde import Balde
jogo = int(input('Digite o número: '))

balde = Balde()
if balde.sorteio() == jogo:
    print('Você acertou!')
else:
    print('Voce errou!')