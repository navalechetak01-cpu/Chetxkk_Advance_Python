class Car:
    def travel(self):
        print("Travelling by Car")


class Bike:
    def travel(self):
        print("Travelling by Bike")


class Walking:
    def travel(self):
        print("Travelling by Walking")


class Travel:
    def __init__(self, strategy):
        self.strategy = strategy

    def start(self):
        self.strategy.travel()


# Create objects
car = Car()
bike = Bike()
walking = Walking()

# Use different strategies
travel1 = Travel(car)
travel1.start()

travel2 = Travel(bike)
travel2.start()

travel3 = Travel(walking)
travel3.start()
