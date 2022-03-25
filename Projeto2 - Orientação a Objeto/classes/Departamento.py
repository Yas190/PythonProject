class Departamento:
    def __init__(self, numero, setor):
        self.numero = numero
        self.setor = setor

    def get_numero(self):
        return self.numero

    def get_setor(self):
        return self.setor

    def set_numero(self, numero, inplace=True):
        if inplace:
            self.numero = numero
        else:
            return Departamento(numero, self.setor)

    def set_setor(self, setor, inplace=True):
        if inplace:
            self.setor = setor
        else:
            return Departamento(self.numero, setor)
