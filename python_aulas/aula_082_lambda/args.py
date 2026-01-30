def add(*args):
    sum = 0
    for valor in args:
        sum += valor
    return sum


def run(funcion, *args):
    return funcion(*args)


print(run(lambda *args: sum(args), 5, 8, 2))  # soma = 15

print(add(3, 5, 7, 1, 2, 8))  # soma = 26
