import pprint


def pp(item):
    pprint.pprint(item, sort_dicts=False, width=50)


word = input('Digite uma palavra um experimento: ')

simbols = [
    [(letra, x) for letra in word]
    for x in range(3)
]

pp(simbols)
