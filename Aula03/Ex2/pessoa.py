class Pessoa:
    # Método construtor (Chamado durante a criação de um objeto)
    def __init__(self, nome:str, sobrenome:str, idade:int) -> None:
        # Atributo (Variáveis da classe com valores passados para o construtor)
        self.__nome = ''
        self.__sobrenome = ''
        self.__idade = 0

        if type(nome) == str:
            self.__nome = nome
        if type(sobrenome) == str:
            self.__sobrenome = nome
        if type(idade) == int:
            self.__idade

    def __verifica_nome(self, nome) -> bool:
        if type(nome) == str:
            return True
        else:
            return False

    def __verifica_sobrenome(self, sobrenome) -> bool:
        if type(sobrenome) == str:
            return True
        else:
            return False

    def __verifica_idade(self, idade) -> bool:
        if type(idade) == int and idade >0:
            return True
        else:
            return False

    def set_nome(self, nome:str) -> None:
        if self.__verifica_nome(nome):
            self.__nome = nome

    def set_sobrenome(self, sobrenome:str) -> None:
        if self.__verifica_sobrenome(sobrenome):
            self.__sobrenome = sobrenome

    def set_idade(self, idade:int) -> None:
        if self.__verifica_idade(idade):
            self.__idade = idade

    def get_nome(self) -> str:
        return self.__nome

    def get_sobrenome(self) -> str:
        return self.__sobrenome

    def get_idade(self) -> int:
        return self.__idade

if __name__ == '__main__':
    pessoa = Pessoa()
    pessoa.set_nome('Pablo')
    pessoa.set_sobrenome('Schumacher')
    pessoa.set_idade(17)
    print(pessoa.get_nome())
    print(pessoa.get_sobrenome())
    print(pessoa.get_idade())