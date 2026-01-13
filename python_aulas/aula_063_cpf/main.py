"""

Cálculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 10 primeiros dígitos do CPF multiplicando cada um dos valores por uma contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*   7  4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados: 
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9: resultado é 0
Contrário disso: resultado é o valor da conta
    
O primeiro dígito do CPF é 0

"""
while True:
    # O usuário digita o CPF:
    cpf_digitado = input('Digite seu CPF: ').strip()

    # Eliminando pontos, espaços e hífens
    cpf_formatado = cpf_digitado \
        .replace('.', '') \
        .replace('-', '') \
        .replace(' ', '')

    # Caso o CPF não tenha 11 dígitos:
    if len(cpf_formatado) != 11:
        print('ERRO! Digite um CPF com 11 dígitos.')
        continue

    # Caso o usuário digite 11 dígitos repetidos:
    if cpf_formatado[0] * 11 == cpf_formatado:
        print('ERRO! Você digitou 11 números iguais. Mais seriedade, por favor.')

    # Caso o usuário digite algum caractere inválido:
    try:
        int(cpf_formatado)
    except:
        print('ERRO! Digite apenas números, pontos e hífen.')
        print('NÃO DIGITE letras ou outros símbolos.')
        continue

    # Os primeiros nove dígitos
    cpf_nove_digitos = cpf_formatado[:9]
    # O décimo dígito é o primeiro verificador
    cpf_verificador_1 = cpf_formatado[9]

    resultado_1 = 0
    multiplicador_1 = 10

    for digito in cpf_nove_digitos:
        resultado_1 += int(digito) * multiplicador_1
        # A cada dígito que passa, o multiplicador diminui 1
        multiplicador_1 -= 1

    # Multiplica por 10, Divide por 11 e pega o resto
    resultado_final_1 = (resultado_1 * 10) % 11

    digito_1 = 0 if resultado_final_1 > 9 else resultado_final_1

    # Os primeiros dez dígitos são necessários para o segundo verificador
    cpf_dez_digitos = cpf_formatado[:10]
    # O décimo primeiro dígito é o segundo verificador
    cpf_verificador_2 = cpf_formatado[10]

    resultado_2 = 0
    multiplicador_2 = 11

    for digito in cpf_dez_digitos:
        resultado_2 += int(digito) * multiplicador_1
        # A cada dígito que passa, o multiplicador diminui 1
        multiplicador_2 -= 1

    # Multiplica por 10, Divide por 11 e pega o resto
    resultado_final_2 = (resultado_2 * 10) % 11

    digito_2 = 0 if resultado_final_2 > 9 else resultado_final_2

    # Analisando se o CPF é válido
    if str(digito_1) == cpf_verificador_1 and str(digito_2) == cpf_verificador_2:
        resposta = True
    else:
        resposta = False

    print(f'O CPF {cpf_digitado} é válido!') if resposta else print(
        f'O CPF {cpf_digitado} é inválido!')
    break
