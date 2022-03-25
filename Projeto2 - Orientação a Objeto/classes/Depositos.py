class Depositos:
    def __init__(self, numero, endereco):
        self.numero = numero
        self.endereco = endereco

    def get_numero(self):
        return self.numero

    def get_endereco(self):
        return self.endereco

    def set_numero(self, numero, inplace=True):
        if inplace:
            self.numero = numero
        else:
            return Depositos(numero, self.endereco)

    def set_endereco(self, endereco, inplace=True):
        if inplace:
            self.endereco = endereco
        else:
            return Depositos(self.numero, endereco)
