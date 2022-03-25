class Carro:
    def __init__(self, registro, marca):
        self.registro = registro
        self.marca = marca

    def get_registro(self):
        return self.registro

    def get_marca(self):
        return self.marca

    def set_registro(self, registro):
        self.registro = registro

    def set_marca(self, marca):
        self.marca = marca
