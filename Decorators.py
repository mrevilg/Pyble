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