"""

Sets (Tipo set)
Sets em Python são mutáveis, porém aceitam apenas tipos imutáveis como valor interno

Criando um set:
set()
set(iterável)
{1, 2, 3, 4, 5}

Sets são eficientes para remover valores duplicados de iteráveis
- Sets possuem valores únicos;
- Sets não possuem índices;
- Sets não garatem ordem;
- Sets são iteráveis (for, in, not in)

Métodos úteis:
- add -> adiciona
- update -> adiciona iterando
- clear -> limpa
- discard -> deleta valor especificado
- union -> união
- intersection -> interseção
- difference -> diferença
    -> retorna os elementos que estão no primeiro conjunto, mas não no segundo
- symmetric_difference -> diferença simétrica 
    -> retorna os elementos que estão em um dos conjuntos, mas não em ambos

Operadores úteis:
- | (union)
- & (intersection)
- - (difference)
- ^ (symmetric_difference)

"""

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s4 = s1 & s2
s5 = s1 - s2
s6 = s2 - s1
s7 = s1 ^ s2
print(s3, s4, s5, s6, s7, sep='\n')
