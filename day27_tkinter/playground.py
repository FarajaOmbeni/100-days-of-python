'''UNLIMITED POSITIONAL ARGUMENTS IN A FUNCTION'''
def add(*args):
    result = 0
    for n in args:
        result += n
    print(result)

add(4,5,2,3,4)

''' UNLINMITED KEYWORD ARGUMENTS'''
def calculate(n, **kwargs):
    print(kwargs['add'])
    n += kwargs['add']
    n *= kwargs['multiply']
    
    print(n)

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)