from random import randint


class Balde:
    def __init__(self):
        self.__balde = 0
        self.__balde_atual = 0

    def get_volume_balde(self):
        return(self.__balde)

    def set_volume_balde(self, volume_balde):
        if type(volume_balde) == int and volume_balde >=10 and volume_balde <= 50:
            self.__balde = volume_balde
            return self.__balde
        else:
            return False

    def enchendo_balde(self,volume_agua):
        if type(volume_agua) == int and volume_agua > 0:
            self.__balde_atual = self.__balde_atual+volume_agua
            if self.__balde_atual < self.__balde:
                return 'Vazio'
            elif self.__balde_atual == self.__balde:
                return True
            else:
                return False
        else:
            return "ValorError"

    def sorteio(self):
            self.__balde = randint(10,50)
            return self.__balde

# objeto = Balde()
# print(objeto.sorteio_())