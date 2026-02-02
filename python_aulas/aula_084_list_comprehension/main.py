"""

List comprehension em Python

List comprehension é uma forma rápida para criar listas a partir de iteráveis.

"""

numbers = []
for number in range(10):
    numbers.append(number)
print(numbers)

numbers = [number * 2 for number in range(10)]
print(numbers)
