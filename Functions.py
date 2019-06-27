













# Passing Lists to a Function

# 3D Printing service, based on 2D Client Submissions

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print("Printing Model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['some case','robot cape','pie']
completed_models = []

# Here, [:] indactes a copy of the list
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)