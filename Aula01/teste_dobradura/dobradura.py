class Dobradura:
    def get_dobrar(self,numero_dobradura):
        self.dobras = 1
        if type(numero_dobradura) == int and numero_dobradura > 0:
            for i in range(numero_dobradura):
                self.dobras = self.dobras*2
            return (self.dobras)
        else:
            return False