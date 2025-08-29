- - -
Class relationship diagrams:
1. __Association__ = _knows_:

![association](/images/class_interactions/association.png)

```python
class Car:
    def __init__(self, model):
        self.model = model

    def drive(self):
        print(f"{self.model} is being driven.")


class Driver:
    def __init__(self, name):
        self.name = name

    def driver_car(self, car: Car):
        print(f"{self.name} is driving {car.model}")
        car.drive()


car1 = Car("Toyota Corolla")
car2 = Car("BMW X5")

driver = Driver("Mykola")

driver.driver_car(car1)
driver.driver_car(car2)
```
2. __Aggregation__ = _has-a_:

![aggregation](/images/class_interactions/aggregation.png)

```python
from typing import List


class Department:
    def __init__(self, name):
        self.name = name

    def show_department(self):
        print(f"Department: {self.name}")


class University:
    def __init__(self, name):
        self.name = name
        self.departments: List[Department] = []

    def add_department(self, department):
        self.departments.append(department)

    def show_departments(self):
        print(f"University: {self.name}")
        for department in self.departments:
            department.show_department()


department1 = Department("Computer Science")
department2 = Department("Mathematics")

university = University("Oxford University")

university.add_department(department1)
university.add_department(department2)
university.show_departments()
```
3. __Composition__ = _owns_:

![composition](/images/class_interactions/composition.png)

```python
class Room:
    def __init__(self, name):
        self.name = name

    def show_room(self):
        print(f"Room: {self.name}")


class House:
    def __init__(self, address):
        self.address = address
        self.rooms = [
            Room("Living Room"),
            Room("Kitchen"),
            Room("Bedroom"),
        ]

    def show_house(self):
        print(f"House at {self.address} has the following rooms:")
        for room in self.rooms:
            room.show_room()


house = House("123 Main Stree")
house.show_house()
del house
```
4. __Inheritance__ = _is-a_:

![inheritance](/images/class_interactions/inheritance.png)

```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def bark(self):
        print(f"({self.name}, {self.breed}, {self.age}) is barking")


dog1 = Dog("Gavchyk", 3, "Sobachka")
dog1.bark()
```
- - -
