from Aula01.teste_balde.balde import Balde
jogo = 0
balde = Balde()
certo = balde.sorteio()
while jogo != certo:
    jogo = int(input('Digite o número: '))
    if certo == jogo:
        print('Você acertou!')
    else:
        print('Voce errou!')