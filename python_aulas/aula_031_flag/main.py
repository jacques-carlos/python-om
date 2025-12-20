# FLAG / NONE / IS / IS NOT

"""

Flag (Bandeira) - marcar um local
None - não valor
is / is not - é / não é (tipo, valor, identidade)
id - identidade

"""

ordem = False
passou_no_if = None

if ordem:
    passou_no_if = True
    print('Prepare o jantar.')
else:
    print('Não prepare o jantar.')


if passou_no_if is None:
    print('Não passou no if.')
elif passou_no_if is not None:
    print('Passou no if.')
