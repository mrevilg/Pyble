


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

# Here the ** tells Python to create an empty Dictionary
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    # this loop adds additional data from ** to profile dict (line 5)
    for key,value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                                location='princeton',
                                field='physics')
print(user_profile)

#--- Decorators and Functions

# Functions are objects
def add_five(num):
    print (num + 5)

add_five(2) # '()' indicates invocation of executable code

# Functions within functions
def add_five(num):
    def add_two(num): # This def is not public
        return num + 2

    num_plus_two = add_two(num)
    print(num_plus_two + 3)    

add_five(10)

# Returning functions from functions
def getMathFunction(operation): # + or -
    def add(num1, num2):
        return num1 + num2
    def sub(num1, num2):
        return num1 - num2

    if operation == '+':
        return add
    elif operation == '-':
        return sub

add_func = getMathFunction('+')
sub_func = getMathFunction('-')
print(sub_func(10, 3))

# Decorating a function
def printMyName():
    print("Stephen")

def title(printNameFunction):
    def wrapper(): # Wrapper is wrapping def into another def
        print("Mr Super")
        printNameFunction()
    return wrapper

decoratedFunction = title(printMyName) # complicated

decoratedFunction()

# Decorators (easy version, not using complicated)

@title
def printMyName():
    print("Stephen")

printMyName()

# Decorators w/ Parameters

def title(printNameFunction):
    def wrapper(*args, **kwargs): 
        print("Mr Super")
        printNameFunction(*args, **kwargs)
    return wrapper

@title
def printMyName(name):
    print(name)

printMyName("Doffy")
