# args
# kwargs -> keyword arguments (argumentos nomeados)

person = {
    'name': 'Aline',
    'lastname': 'Souza',
    'age': 16,
    'height': 1.6
}


# função para exibir argumentos nomeados
def show_keywords_arguments(*args, **kwargs):
    print('No keywords arguments:', args)
    for key, value in kwargs.items():
        print(f'{key=} | {value=}')


show_keywords_arguments('Hello, World!', 777, True,
                        name='Jacques', lastname='Santos')

print()
show_keywords_arguments(**person)
