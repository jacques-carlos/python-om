texto = 'Python'  # interável
novo_texto = ''

for letra in texto:
    print(letra)

for letra in texto:
    novo_texto += f'*{letra}'

novo_texto += '*'
print(novo_texto)
