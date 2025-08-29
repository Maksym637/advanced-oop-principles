class Animal:
    def __init__(self, name):
        self._name = name


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


def get_pet(pet):
    pets = dict(dog=Dog("Rex"), cat=Cat("Lucy"))
    return pets[pet]


dog = get_pet("dog")
print(dog.speak())

cat = get_pet("cat")
print(cat.speak())
