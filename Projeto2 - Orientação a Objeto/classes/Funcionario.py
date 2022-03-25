class Funcionario:
    def __init__(self, nome, numero, salario, telefone):
        self.nome = nome
        self.numero = numero
        self.salario = salario
        self.telefone = telefone

    def get_nome(self):
        return self.nome

    def get_numero(self):
        return self.numero

    def get_salario(self):
        return self.salario

    def get_telefone(self):
        return self.telefone

    def set_nome(self, nome, inplace=True):
        if inplace:
            self.nome = nome
        else:
            return Funcionario(nome, self.salario, self.telefone)

    def set_numero(self, numero, inplace=True):
        if inplace:
            self.numero = numero
        else:
            return Funcionario(numero, self.salario, self.telefone)

    def set_salario(self, salario, inplace=True):
        if inplace:
            self.salario = salario
        else:
            return Funcionario(self.numero, salario, self.telefone)

    def set_telefone(self, telefone, inplace=True):
        if inplace:
            self.telefone = telefone
        else:
            return Funcionario(self.numero, self.salario, telefone)
