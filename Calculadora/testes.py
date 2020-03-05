from Calculadora.Operacoes import Opecacoes
from Calculadora.Perguntas import Perguntas

n1 = float(input('Informe o primeiro número: '))
n2 = float(input('Informe o segundo número: '))
tipo = int(input('Informe o tipo de operação que deseja: '))
operacoes = Opecacoes(n1,n2)
perguntas = Perguntas(n1,n2,tipo)

print('Iniciando os testes! \n')

print('Teste de atribuição de n1 iniciado')
assert n1 == perguntas.set_n1(n1), 'Erro! A atribuição de n1 não foi feita!'
print('Teste de atribuição de n1: Ok')

print('Teste de atribuição de n2 iniciado')
assert n2 == perguntas.set_n2(n2), 'Erro! A atribuição de n2 não foi feita!'
print('Teste de atribuição de n2: Ok')

print('Teste de atribuição de tipo iniciado')
assert tipo == perguntas.set_tipo(tipo), 'Erro! A atribuição de tipo não foi feita!'
print('Teste de atribuição de tipo: Ok')

print('Teste da operacao soma() iniciado')
assert n1+n2 == operacoes.soma(n1,n2), f'Erro! A soma entre {n1} e {n2} não deu {n1+n2}!'
print('Teste da operacao soma(): Ok \n')

print('Teste da operacao subtracao() iniciado')
assert n1-n2 == operacoes.subtracao(n1,n2), f'Erro! A subtracao entre {n1} e {n2} não deu {n1-n2}!'
print('Teste da operacao subtracao(): Ok \n')

print('Teste da operacao multiplicacao() iniciado')
assert n1*n2 == operacoes.multiplicacao(n1,n2), f'Erro! A multiplicacao entre {n1} e {n2} não deu {n1*n2}!'
print('Teste da operacao multiplicacao(): Ok \n')

print('Teste da operacao divisao_decimal() iniciado')
assert n1/n2 == operacoes.divisao_decimal(n1,n2), f'Erro! A divisao decimal entre {n1} e {n2} não deu {n1/n2}!'
print('Teste da operacao divisao_decimal(): Ok \n')

print('Teste da operacao divisao_exata() iniciado')
assert n1//n2 == operacoes.divisao_exata(n1,n2), f'Erro! A divisao exata entre {n1} e {n2} não deu {n1//n2}!'
print('Teste da operacao divisao_exata(): Ok \n')

print('Teste da operacao resto() iniciado')
assert n1%n2 == operacoes.resto(n1,n2), f'Erro! O resto da divisão entre {n1} e {n2} não deu {n1%n2}!'
print('Teste da operacao resto(): Ok \n')

print('Teste de get_resposta() iniciado')
if tipo == 1:
    assert operacoes.soma(n1,n2) == perguntas.get_resposta(n1,n2,tipo)
elif tipo == 2:
    assert operacoes.subtracao(n1,n2) == perguntas.get_resposta(n1,n2,tipo)
elif tipo == 3:
    assert operacoes.multiplicacao(n1,n2) == perguntas.get_resposta(n1,n2,tipo)
elif tipo == 4:
    assert operacoes.divisao_decimal(n1,n2) == perguntas.get_resposta(n1,n2,tipo)
elif tipo == 5:
    assert operacoes.divisao_exata(n1,n2) == perguntas.get_resposta(n1,n2,tipo)
elif tipo == 6:
    assert operacoes.resto(n1,n2) == perguntas.get_resposta(n1,n2,tipo)
print('Teste de get_resposta(): Ok \n')