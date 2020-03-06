from Aula03.Ex2.endereco import Endereco
from Aula03.Ex2.pessoa import Pessoa

pessoa = Pessoa()
pessoa.set_nome('Pablo')
pessoa.set_sobrenome('Schumacher')
pessoa.set_idade(17)
print(pessoa.get_nome())
print(pessoa.get_sobrenome())
print(pessoa.get_idade())

endereco = Endereco()
endereco.set_cidade('Blumenau')
endereco.set_rua('Everestes')
endereco.set_numero(129)
print(endereco.get_cidade())
print(endereco.get_rua())
print(endereco.get_numero())