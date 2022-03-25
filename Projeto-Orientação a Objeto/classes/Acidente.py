class Acidente:
    def __init__(self, data, hora, local):
        self.data = data
        self. hora = hora
        self.local = local

    def get_data(self):
        return self.data

    def get_hora(self):
        return self.hora

    def get_local(self):
        return self.local

    def set_data(self, data, inplace=True):
        if inplace:
            self.data = data
        else:
            return Acidente(data, self.hora, self.local)

    def set_local(self, local, inplace=True):
        if inplace:
            self.local = local
        else:
            return Acidente(self.data, self.hora, local)
