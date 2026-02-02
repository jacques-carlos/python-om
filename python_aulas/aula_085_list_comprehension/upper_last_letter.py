names = ['luiz', 'maria', 'helena', 'joana', 'felipe']
new_names = [
    f'{name[:-1].lower()}{name[-1].upper()}'
    for name in names
]
print(new_names)
