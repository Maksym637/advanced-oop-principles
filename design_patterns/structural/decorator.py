from abc import ABC, abstractmethod


# Component
class Coffee(ABC):
    @abstractmethod
    def cost(self) -> float:
        pass

    @abstractmethod
    def description(self) -> str:
        pass


# Concrete Component
class SimpleCoffee(Coffee):
    def cost(self) -> float:
        return 2.0

    def description(self) -> str:
        return "Simple Coffee"


# Base Decorator
class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee):
        self._coffee = coffee

    def cost(self) -> float:
        return self._coffee.cost()

    def description(self) -> str:
        return self._coffee.description()


# Concrete Decorators
class MilkDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return super().cost() + 0.5

    def description(self) -> str:
        return super().description() + ", Milk"


class SugarDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return super().cost() + 0.2

    def description(self) -> str:
        return super().description() + ", Sugar"


class WhipCreamDecorator(CoffeeDecorator):
    def cost(self) -> float:
        return super().cost() + 0.7

    def description(self) -> str:
        return super().description() + ", Whip Cream"


coffee = SimpleCoffee()
print(f"{coffee.description()} -> ${coffee.cost()}")

coffee = WhipCreamDecorator(SugarDecorator(MilkDecorator(coffee)))
print(f"{coffee.description()} -> ${coffee.cost()}")
