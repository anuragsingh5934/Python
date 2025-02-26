def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current = unprinted_designs.pop()
        print(f"printing {current}.")
        completed_models.append(current)
def show_completed_models(completed_models):
    for models in completed_models:
        print(models)

unprinted_models = ['iphone','samsung','oppo','vivo','razor','oneplus','tenor']
completed_models = []

print_models(unprinted_models,completed_models)
show_completed_models(completed_models)
