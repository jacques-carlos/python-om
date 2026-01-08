"""

Faça uma lista de comprar (com listas)
O usuário deve ter a possibilidade de:
Inserir, apagar, e listar valores da sua lista
Não permita que o programa quebre com erros de índices inexistentes na lista.

"""

from os import system

system('cls')
lista_de_compras = []

while True:

    print('1: Inserir item | 2: Apagar item | 3: Listar itens | 4: Sair')
    resposta_ = input('O que você deseja fazer? ')

    try:
        resposta = int(resposta_)

    except:
        print('Ocorreu um erro. Tente novamente.')

    else:
        # Adicionar item
        if resposta == 1:
            item = input('Qual item você deseja adicionar? ')
            lista_de_compras.append(item)

        # Remover item
        elif resposta == 2:
            retorno = input(
                'Qual item você deseja remover? (Informe o índice): ')

            try:
                indice = int(retorno)
                item_deletado = lista_de_compras.pop(indice)
            except:
                print('Erro! Esse item (índice) não existe. Tente novamente.')
            else:
                print(f'Item "{item_deletado}" deletado com sucesso.')

        # Listar itens
        elif resposta == 3:
            system('cls')
            if bool(lista_de_compras):
                print('Lista de Compras:'.center(30))
                for ind, item in enumerate(lista_de_compras):
                    print(ind, item)
            else:
                print('Nada para listar.')

        # Sair do sistema
        elif resposta == 4:
            print('Volte sempre!')
            break

        # Usuário selecionou uma opção inexistente:
        else:
            print('Erro! Digite uma opção válida.')
            continue
