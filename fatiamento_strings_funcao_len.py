"""
Fatiamento de string:
012345678
Olá mundo
-987654321
Fatiamento [i:f:p]
Obs.: a função len retorna a quantidade 
de caracteres da st

"""

variavel = 'Olá mundo'
print(variavel[4:10]) # os dois pontos ':' indica exatamento o fatiamento
print(len(variavel))
print(variavel[0:9:2]) # o '2' significa os passos que estou dando na minha str
print(variavel[::-1])