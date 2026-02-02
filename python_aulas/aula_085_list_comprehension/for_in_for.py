# for dentro de for em list comprehension

# criando uma lista na forma tradicional
numbers_1 = []

for x in range(3):
    for y in range(3):
        numbers_1.append((x, y))

print(numbers_1)


# criando uma lista com list comprehension
numbers_2 = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

print(numbers_2)
