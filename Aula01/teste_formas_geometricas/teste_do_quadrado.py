from Aula01.teste_formas_geometricas.quadrado import Quadrado

lateral = 3
quadrado = Quadrado(lateral)

print('Iniciando os testes! \n')

print('Teste de atribuição do valor de lateral para a criação da classe')
assert lateral == quadrado._Quadrado__lateral, f'Erro! A lateral: {lateral} não está sendo passada para o objeto na inicialização!'
print('Teste de atribuição do valor de lateral para a criação da classe: Ok \n')

print('Teste do set_lateral()')
quadrado.set_lado(1)
assert 1 == quadrado._Quadrado__lateral, f'Erro! A lateral: {lateral} não está sendo passada para o objeto!'
print('Teste do set_lado(): Ok \n')

print('Teste do get_lateral()')
lateral = 2
quadrado.set_lado(lateral)
assert lateral == quadrado.get_lado(lateral), f'Erro! A lateral: {lateral} não está sendo passada para o objeto!'
print('Teste do get_lado(): Ok \n')

print('Teste do calcular_area()')
assert lateral * lateral == quadrado.calcular_area(lateral), f'Erro! O cálculo de área nao está retornando correto!'
print('Teste do calculo de área: Ok \n')
