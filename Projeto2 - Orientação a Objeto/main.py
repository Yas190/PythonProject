from classes.Funcionario import Funcionario
from classes.Departamento import Departamento
from classes.Fornecedor import Fornecedor
from classes.Pecas import Pecas
from classes.Projeto import Projeto
from classes.Depositos import Depositos

funcionario1 = Funcionario('Irineu', 126, 1500, '(21)972296697')

peca1 = Pecas(4, 'Leroy Merlin', 1, 'Cinza')
peca2 = Pecas(12, 'Cocil',  0.4, 'Verde')

lista_pecas = [peca1.get_id_peca(), peca2.get_id_peca()]
lista_fornecedor = [peca1.get_fornecedor(), peca2.get_fornecedor()]

projeto1 = Projeto(200, lista_pecas, 2530)

print(projeto1.get_pecas_usadas())
print(peca2.get_fornecedor())