











#----

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

#----

# Passing an arbitrary number of arguments

# the '*' tells Py to create an empty tuple
def make_pizza(*toppings):
    """Summarize the pizza we're about to make"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', "green peppers", "corn")


# Mixing positional and arbitrary arguments

def make_pizza_(size, *toppings):
    """Summarize the pizza we're about to make"""
    print("\nMaking a " +str(size) + 
        "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza_(16, 'pepperoni')
make_pizza_(12, 'mushrooms', "green peppers", "corn")


#----