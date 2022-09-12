""" Exercício back-end Fábrica 2022.2"""

x = float(input('Insira o Valor do produto: ')) 
y = float(input('Insira a porcentagem do desconto a ser dado: ')) 
 
from modulo_atv1 import porcentagem_desconto

print (porcentagem_desconto(x,y))
