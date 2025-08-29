class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)

        return cls._instance

    def __init__(self):
        self.value = 42


singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # True
print(singleton1.value, singleton2.value)

singleton1.value = 100
print(singleton1.value, singleton2.value)
