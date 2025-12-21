# CALCULADORA COM WHILE

#  variáveis:
entrada_1 = entrada_2 = operador = sair = ''  # str
valor_1 = valor_2 = resultado = 0  # int

while True:
    resultado = 0  # o resultado sempre zera a cada repetição
    sair = 'Sem resposta'  # a resposta sempre "zera" também
    print('='*30)
    print('CALCULADORA'.center(30))
    entrada_1 = input('PRIMEIRO VALOR: ')  # pede primeiro valor
    entrada_2 = input('SEGUNDO VALOR: ')  # pede segundo valor
    # informa os operadores
    print('mais: +\nmenos: -\nmultiplicação: *\ndivisão: /')
    operador = input('OPERADOR: ')  # pede operador

    try:
        valor_1 = int(entrada_1)  # tenta "converter" em inteiro
        valor_2 = int(entrada_2)  # tenta "converter" em inteiro

    except:
        # caso não seja possível "converter" para inteiro:
        print('Erro! Digite valores inteiros.')

    else:
        # se o operador for "+" os resultados somam-se
        if operador == '+':
            resultado = valor_1 + valor_2
            # retornar o resultado
            print(f'{entrada_1} {operador} {entrada_2} = {resultado}')

        # se o operador for "-" os resultados subtraem-se
        elif operador == '-':
            resultado = valor_1 - valor_2
            # retornar o resultado
            print(f'{entrada_1} {operador} {entrada_2} = {resultado}')

        # se o operador for "*" os resultados multiplicam-se
        elif operador == 'x' or operador == '*':
            resultado = valor_1 * valor_2
            # retornar o resultado
            print(f'{entrada_1} {operador} {entrada_2} = {resultado}')

        # se o operador for "/" os resultados dividem-se
        elif operador == '/':
            resultado = valor_1 / valor_2
            # retornar o resultado com duas casas decimais
            print(f'{entrada_1} {operador} {entrada_2} = {resultado:.2f}')

        # caso o usuário digite qualquer coisa que não seja um operador
        else:
            print('Erro! Digite um operador válido.')

    finally:
        # pergunta se o usuário deseja sair do programa
        while sair not in 'SsNn':
            sair = input('Deseja sair da calculadora? [S/N]: ').strip()
        if sair in 'Ss':
            print('Encerrando o programa... Até mais!')
            break
