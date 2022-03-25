from classes.Acidente import Acidente
from classes.Apolice import Apolice
from classes.Carro import Carro
from classes.Cliente import Cliente

cliente1 = Cliente('(21)972296697', 'Yasmin Pires', 'RS-287')

print(cliente1.get_nome())
cliente1.set_endereco("Caronchinha")
print(cliente1.get_endereco())
