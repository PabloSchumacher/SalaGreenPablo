class Endereco:
    # Método construtor (Chamado durante a criação de um objeto)
    def __init__(self) -> None:
        # Atributo (Variáveis da classe com valores default)
        self.__cidade = ''
        self.__rua = ''
        self.__numero = 0

    def __verifica_cidade(self, cidade) -> bool:
        if type(cidade) == str:
            return True
        else:
            return False

    def __verifica_rua(self, rua) -> bool:
        if type(rua) == str:
            return True
        else:
            return False

    def __verifica_numero(self, numero) -> bool:
        if type(numero) == int:
            return True
        else:
            return False

    def set_cidade(self,cidade:str) -> None:
        if self.__verifica_cidade(cidade):
            self.__cidade = cidade

    def set_rua(self, rua:str) -> None:
        if self.__verifica_rua(rua):
            self.__rua = rua

    def set_numero(self, numero:int) -> None:
        if self.__verifica_numero(numero):
            self.__numero = numero

    def get_cidade(self) -> str:
        return self.__cidade

    def get_rua(self) -> str:
        return self.__rua

    def get_numero(self) -> int:
        return self.__numero

if __name__ == '__main__':
    endereco = Endereco()
    endereco.set_cidade('Blumenau')
    endereco.set_rua('Everestes')
    endereco.set_numero(129)
    print(endereco.get_cidade())
    print(endereco.get_rua())
    print(endereco.get_numero())