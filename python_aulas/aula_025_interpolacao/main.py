"""

Interpolação básica de strings
s -> string
d e i -> int
f -> float
x e X -> hexadecimal (ABCDEF0123456789)

"""

nome = 'Otávio'
preco = 1000.95897643
saudacao = 'Olá, %s' % nome
variavel = '%s, o preço é R$ %.2f' % (nome, preco)
print(saudacao)
print(variavel)
print('O hexadecimal de %d é %08x' % (15, 15))
