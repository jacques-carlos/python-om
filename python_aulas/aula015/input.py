nome = input('Qual é o seu nome? ')
print(f'Seu nome é {nome}')
print(f'{nome=}')  # Mostra o nome da variável e o valor da variável


# int(input('Digite um número: ')) pode gerar problemas
numero1 = input('Digite um número: ')
numero2 = input('Digite outro número: ')

int_numero1 = int(numero1)
int_numero2 = int(numero2)

print(f'A soma dos números é {int_numero1 + int_numero2}')
