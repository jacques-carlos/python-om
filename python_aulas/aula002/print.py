# CRLF      -> \r\n
# LF        -> \n

print(12, 34, sep='-', end='\r\n')
print(56, 78, sep='#', end='\n')
print(90, 555, end='%%')
print('Olá!', end='##\n')           # Quebra de linha + caracteres.
print('Tchau!')

# Print é um Função. Toda Função possui Argumentos.
# Argumentos Nomeados (ex.):
# Argumento sep: separador.
# Argumento end: quebra de linha.
