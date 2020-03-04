class Endereco:
    def __init__(self, estado,cidade, rua, numero):
        self.__estado = estado
        self.__cidade = cidade
        self.__rua = rua
        self.__numero = numero

    def set_estado(self, estado):
        self.__estado = estado

    def set_cidade(self, cidade):
        self.__cidade = cidade

    def set_rua(self, rua):
        self.__rua = rua

    def set_numero(self, numero):
        self.__numero = numero

    def get_estado(self):
        return self.estado

    def get_cidade(self):
        return self.estado

    def get_rua(self):
        return self.rua

    def get_numero(self):
        return self.numero



class Pessoa():
    def __init__(self, nome, sobrenome, idade, estado, cidade, rua, numero):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__idade = idade
        self.endereco = Endereco(estado, cidade, rua, numero)

    def set_nome(self,nome):
        self.__nome = nome

    def set_sobrenome(self,sobrenome):
        self.__sobrenome = sobrenome

    def set_idade(self,idade):
        self.__idade = idade

    def get_nome(self):
        return self.__nome

    def get_sobrenome(self):
        return self.__sobrenome

    def get_idade(self):
        return self.__idade

    # def set_endereco(self, estado, cidade, rua, numero):
    #     self.endereco.set_estado(estado)
    #     self.endereco.set_cidade(cidade)
    #     self.endereco.set_rua(rua)
    #     self.endereco.set_numero(numero)

class Engenheiro(Pessoa):
    def __init__(self, esepc, estado_civil, nome, sobrenome, idade, estado, cidade, rua, numero):
        self.__espec = esepc
        self.__estado_civil = estado_civil
        super().__init__(nome, sobrenome, idade, estado, cidade, rua, numero)
    def set_espec(self, espec):
        self.__espec = espec
    def get_espec(self):
        return self.__espec
    def set_estado_civil(self, estado_civil):
        self.__estado_civil = estado_civil
    def get_estavo_civil(self):
        return self.__estado_civil

if __name__ == '__main__':
    pessoa = Pessoa('','',0,'','','',0)
    pessoa.set_nome(input('Informe o nome: '))
    print(pessoa.get_nome())
    pessoa.endereco.set_estado(input('Informe seu estado: '))
    pessoa.endereco.set_cidade(input('Informe sua cidade: '))
    pessoa.endereco.set_rua(input('Informe sua rua: '))
    pessoa.endereco.set_numero(input('Informe seu numero: '))
    a = Engenheiro('','','','',0,'','','',0)
    a.set_nome(input('Informe o seu número Sr. Engenheiro: '))
    print(a.get_nome())