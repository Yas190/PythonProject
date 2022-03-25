class Cliente:
    def __init__(self, numero, nome, endereco):
        self.numero = numero
        self. nome = nome
        self.endereco = endereco

    def get_numero(self):
        return self.numero

    def get_nome(self):
        return self.nome

    def get_endereco(self):
        return self.endereco

    def set_nome(self, nome):
        self.nome = nome

    def set_numero(self, numero):
        self.numero = numero

    def set_endereco(self, endereco):
        self.endereco = endereco
