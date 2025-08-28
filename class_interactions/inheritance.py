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
