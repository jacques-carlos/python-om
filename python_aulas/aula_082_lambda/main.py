def run(funcion, *args):  # Função para executar uma função (lambda incluso)
    return funcion(*args)


def add(x, y):  # Função somar
    return x + y


def make_multiplication(multiplier):  # Função criar uma multiplicação
    def multiply(number):  # Função multiplicar
        return number * multiplier
    return multiply


# Maneiras diferentes de executar a função add
print(add(10, 20))
print(run(add, 10, 20))
print(run(lambda x, y: x + y, 10, 20))

# Maneiras diferentes de executar a função make_multiplication
double = make_multiplication(2)
triple = run(make_multiplication, 3)
quadruple = run(lambda m: lambda n: m * n, 4)

print(double(5))
print(triple(5))
print(quadruple(5))
