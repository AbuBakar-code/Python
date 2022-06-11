# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum

# print(add(2, 3, 4, 5))

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get('name')
        self.modle = kwargs.get('modle')
        self.color = kwargs.get('color')

car = Car(make='Porche', modle='cayman', color='black')
print(car.modle)