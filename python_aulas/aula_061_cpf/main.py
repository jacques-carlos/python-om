"""

Cálculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF multiplicando cada um dos valores por uma contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*   7  4  6  8  2  4  8  9  0
   70 36 48 56 12 20 32 27  0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9: resultado é 0
Contrário disso: resultado é o valor da conta
    
O primeiro dígito do CPF é 7

"""
while True:
    # O usuário digita o CPF:
    cpf_digitado = input('Digite seu CPF: ').strip()

    # Formatação do CPF para eliminar hífen e pontos:
    cpf_formatado = cpf_digitado.split('.')
    cpf_formatado = ''.join(cpf_formatado)  # CPF sem pontos
    cpf_formatado = cpf_formatado.split('-')
    cpf_formatado = ''.join(cpf_formatado)  # CPF sem hífen e sem pontos

    if len(cpf_formatado) != 11:
        print('ERRO! Digite um CPF com 11 dígitos.')
        continue

    try:
        int(cpf_formatado)
    except:
        print('ERRO! Digite apenas números, pontos e hífen.')
        print('NÃO DIGITE letras, outros símbolos ou espaços.')
        continue

    # CPF base: os primeiros nove dígitos
    cpf_base = cpf_formatado[:9]
    # O décimo dígito é o primeiro verificador (o foco desse exercício)
    cpf_verificador_1 = cpf_formatado[9]

    resultado = 0
    multiplicador = 10

    for digito in cpf_base:
        # Multiplica e soma ao resultado
        resultado += int(digito) * multiplicador
        # A cada dígito que passa, o multiplicador diminui 1
        multiplicador -= 1

    # Multiplica por 10, Divide por 11 e pega o resto
    resultado_final = (resultado * 10) % 11
    # Encontra o resultado final
    digito_1 = 0 if resultado_final > 9 else resultado_final

    resposta = True if str(
        digito_1) == cpf_verificador_1 else False

    print('O CPF é válido, por enquanto...') if resposta else print(
        'O CPF é inválido!')
    break
