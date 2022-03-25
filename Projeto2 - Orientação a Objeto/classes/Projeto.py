class Projeto:
    def __init__(self, numero, pecas_usadas, orcamento):
        self.numero = numero
        self.pecas_usadas = pecas_usadas
        self.orcamento = orcamento

    def get_numero(self):
        return self.numero

    def get_pecas_usadas(self):
        return self.pecas_usadas

    def get_orcamento(self):
        return self.orcamento

    def set_numero(self, numero, inplace=True):
        if inplace:
            self.numero = numero
        else:
            return Projeto(numero, self.pecas_usadas, self.orcamento)

    def set_pecas_usadas(self, pecas_usadas, inplace=True):
        if inplace:
            self.pecas_usadas = pecas_usadas
        else:
            return Projeto(self.numero, pecas_usadas, self.orcamento)

    def set_orcamento(self, orcamento, inplace=True):
        if inplace:
            self.orcamento = orcamento
        else:
            return Projeto(self.numero, self.pecas_usadas, orcamento)
