unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
complete_models = []

while unprinted_designs:
    current = unprinted_designs.pop()
    print(f'printing {current}')
    complete_models.append(current)


print(f"\nThe following models have been printed ")
for com in complete_models:
    print(com)