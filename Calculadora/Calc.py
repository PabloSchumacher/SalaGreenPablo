from Calculadora.Perguntas import Perguntas

calc = Perguntas(0,0,0)
n1 = calc.set_n1(0)
tipo = calc.set_tipo(0)
n2 = calc.set_n2(0)
print(calc.get_resposta(n1,n2,tipo))