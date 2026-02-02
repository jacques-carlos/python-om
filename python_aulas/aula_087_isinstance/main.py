# isinstance - para saber se o objeto é de determinado tipo

stuff = [
    'a', 7, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'}
]


for item in stuff:
    if isinstance(item, set):
        print('set:')
        item.add(10)
        print(item)

    elif isinstance(item, str):
        print('str:')
        print(item.upper())

    elif isinstance(item, (int, float)):
        print('num:')
        item *= 5
        print(item)

    else:
        print('others')
        print(item)
