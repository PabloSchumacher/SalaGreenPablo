from Aula01.teste_formas_geometricas.retangulo import Retangulo

base = 5
altura = 2

retangulo = Retangulo(base, altura)

print('Iniciando os testes! \n')

print('Teste de atribuição do valor de base para a criação da classe')
assert base == retangulo._Retangulo__base, f'Erro! A base: {base} não está sendo passada para o objeto na inicialização!'
print('Teste de atribuição do valor de base para a criação da classe: Ok \n')

print('Teste de atribuição do valor de altura para a criação da classe')
assert altura == retangulo._Retangulo__altura, f'Erro! A altura: {altura} não está sendo passada para o objeto na inicialização!'
print('Teste de atribuição do valor de altura para a criação da classe: Ok \n')

print('Teste do set_base()')
retangulo.set_base(6)
assert 6 == retangulo._Retangulo__base, f'Erro! A base: {base} não está sendo passada para o objeto!'
print('Teste do set_base(): Ok \n')

print('Teste do get_base()')
base = 7
retangulo.set_base(base)
assert base == retangulo.get_base(), f'Erro! A base: {base} não está sendo passada para o objeto!'
print('Teste do get_base(): Ok \n')

print('Teste do set_altura()')
retangulo.set_altura(3)
assert 3 == retangulo._Retangulo__altura, f'Erro! A altura: {altura} não está sendo passada para o objeto!'
print('Teste do set_altura(): Ok \n')

print('Teste do get_altura()')
altura = 4
retangulo.set_altura(altura)
assert altura == retangulo.get_altura(),  f'Erro! A altura: {altura} não está sendo passada para o objeto!'
print('Teste do get_altura(): Ok \n')

print('Teste do calcular_area()')
assert base*altura == retangulo.calcular_area(base,altura), f'Erro! O cálculo de área nao está retornando correto!'
print('Teste do calculo de área: Ok \n')
