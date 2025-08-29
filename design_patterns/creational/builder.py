from abc import ABC, abstractmethod


class Car:
    def __init__(self):
        self.engine = None
        self.wheels = None
        self.color = None

    def __str__(self):
        return f"Car(engine={self.engine}, wheels={self.wheels}, color={self.color})"


class CarBuilder(ABC):
    @abstractmethod
    def set_engine(self):
        pass

    @abstractmethod
    def set_wheels(self):
        pass

    @abstractmethod
    def set_color(self):
        pass

    @abstractmethod
    def get_result(self):
        pass


class SportsCarBuilder(CarBuilder):
    def __init__(self):
        self.car = Car()

    def set_engine(self):
        self.car.engine = "V8 Turbo"

    def set_wheels(self):
        self.car.wheels = "18-inch Alloy"

    def set_color(self):
        self.car.color = "Red"

    def get_result(self):
        return self.car


class SUVBuilder(CarBuilder):
    def __init__(self):
        self.car = Car()

    def set_engine(self):
        self.car.engine = "V6 Diesel"

    def set_wheels(self):
        self.car.wheels = "20-inch Off-road"

    def set_color(self):
        self.car.color = "Black"

    def get_result(self):
        return self.car


class Director:
    def __init__(self, builder: CarBuilder):
        self._builder = builder

    def construct_car(self):
        self._builder.set_engine()
        self._builder.set_wheels()
        self._builder.set_color()
        return self._builder.get_result()


for builder in [SportsCarBuilder(), SUVBuilder()]:
    director = Director(builder)
    print(director.construct_car())
