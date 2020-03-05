from Aula01.teste_formas_geometricas.circulo import Circulo
import math

cor = 'Preto'
raio = 5
material = 'cobre'
circulo = Circulo(cor,raio,material)

print('Iniciando os testes! \n')

print('Teste de atribuição do valor de cor para a criação da classe')
assert cor == circulo._Circulo__cor, f'Erro! A cor: {cor} não está sendo passada para o objeto na inicialização!'
print('Teste de atribuição do valor de cor para a criação da classe: Ok \n')

print('Teste de atribuição do valor de cor para a criação da classe')
assert material == circulo._Circulo__material, f'Erro! O material: {material} não está sendo passada para o objeto na inicialização!'
print('Teste de atribuição do valor de material para a criação da classe: Ok \n')

print('Teste de atribuição do valor de raio para a criação da classe')
assert raio == circulo._Circulo__raio, f'Erro! O raio: {raio} não está sendo passada para o objeto na inicialização!'
print('Teste de atribuição do valor de raio para a criação da classe: Ok \n')

print('Teste do set_cor()')
circulo.set_cor('Branco')
# assert 'Branco' == circulo.get_cor(cor), f'Erro! A cor: {cor} não está sendo passada para o objeto!'
assert 'Branco' == circulo._Circulo__cor, f'Erro! A cor: {cor} não está sendo passada para o objeto!'
print('Teste do set_cor(): Ok \n')

print('Teste do get_cor()')
cor = 'Vermelho'
circulo.set_cor(cor)
assert cor == circulo.get_cor(), f'Erro! A cor: {cor} não está sendo passada para o objeto!'
print('Teste do set_cor(): Ok \n')

print('Teste do calcular_area()')
assert math.pi*raio**2 == circulo.calcular_area(raio), f'Erro! O cálculo de área nao está retornando correto!'
print('Teste do calculo de área: Ok \n')

