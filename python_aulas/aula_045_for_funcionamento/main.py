"""

Iterável -> str, range, etc.
__iter__() -> dunder
Iterador -> quem sabe entregar um valor por vez
__next__() -> dunder

iter() -> me entregue seu iterador
next() -> me entregue o próximo valor

"""

"""
for letra in texto:
    print(letra)
"""

texto = 'Abacaxi'  # interável
iterador = iter(texto)   # iterator

while True:
    try:
        letra = next(iterador)
        print(letra)

    except StopIteration:
        break
