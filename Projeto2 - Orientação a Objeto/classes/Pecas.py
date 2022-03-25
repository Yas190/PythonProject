class Pecas:
    def __init__(self, id_peca, fornecedor, peso, cor):
        self.id_peca = id_peca
        self.fornecedor = fornecedor
        self.peso = peso
        self.cor = cor

    def get_id_peca(self):
        return self.id_peca

    def get_fornecedor(self):
        return self.fornecedor

    def get_peso(self):
        return self.peso

    def get_cor(self):
        return self.cor

    def set_id_peca(self, id_peca, inplace=True):
        if inplace:
            self.id_peca = id_peca
        else:
            return Pecas(id_peca, self.fornecedor, self.peso, self.cor)

    def set_peso(self, peso, inplace=True):
        if inplace:
            self.peso = peso
        else:
            return Pecas(self.id_peca, self.fornecedor, peso, self.cor)

    def set_telefone(self, cor, inplace=True):
        if inplace:
            self.cor = cor
        else:
            return Pecas(self.id_peca, self.fornecedor, self.peso, cor)
