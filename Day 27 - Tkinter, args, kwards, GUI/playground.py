#   Unlimited positional arguments *args


# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum

# print(add(3, 5, 6))

# Keyword arguments **kwargs

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n*= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

my_car = Car(make="VW", model="jetta")

print(my_car.model)